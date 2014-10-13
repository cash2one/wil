#!/usr/bin/env python3

attributes = dict(
    cooldown=bool,
    name=str,
    number=float,
    lv=int,
    exp=int,
    hp=int,
    maxhp=int,
    mp=int,
    maxmp=int,
    maxexp=int,
    weight=int,
    maxweight=int,
    bag=list,
    friends=list,
    tasks=object,
    happy=bool,
)

types = {
    str: "String",
    int: "int",
    float: "Number",
    bool: "Boolean",
    list: "Object",
    object: "Object",
}

defaults = {
    str: '"foo"',
    int: "0",
    float: "0",
    bool: "false",
    list: "[]",
    object: "{}",
}

defines = {
    str: "var",
    int: "var",
    float: "var",
    bool: "var",
    list: "const",
    object: "const",
}

src = """
{% autoescape None %}
package mir  {
    import flash.events.Event;
    import flash.events.EventDispatcher;
    import mx.utils.StringUtil;

    public final class Player extends EventDispatcher {
        public static const self:Player = new Player();

    {% for a, t in attributes %}

        private {{ defines[t] }} _{{ a }}:{{ types[t] }} = {{ defaults[t] }};

        public function get {{ a }}():{{ types[t] }} { return _{{ a }}; }

        public function set {{ a }}(_:{{ types[t] }}):void {

        {% if t == list %}

            for (var k:String in _) {
                _{{ a }}[k] = _[k];
            }

        {% elif t == object %}

            for (var k:String in _) {
                if (_[k] === null) {
                    delete _{{ a }}[k];
                } else {
                    _{{ a }}[k] = _[k];
                }
            }

        {% else %}

            _{{ a }} = _;

        {% end %}

            dispatchEvent(new Event("{{ a }}"));
        }

        {% if t in {int, float} %}

        public function set {{ a }}Delta(_:{{ types[t] }}):void {
            _{{ a }} += _;
            dispatchEvent(new Event("{{ a }}"));
        }

        {% end %}

    {% end %}

        public function set ox(attr:String):void {
            this[attr] = !this[attr];
        }

        public function bindView(notation:String, view:Function):void {
            const player:Player = this;
            const commands:Array = [];

            function model():Array {
                /** copy from Calc.rpn */
                const stack:Array = [];
                var x:*, a:Number, b:Number;
                for each (x in commands){
                    if (x is Number) {
                        stack.push(x);
                    } else if (x is String) {
                        stack.push(player[x]);
                    } else {
                        const args:Array = [];
                        var n:int = x.length;
                        while (n--) {
                            args.unshift(stack.pop());
                        }
                        stack.push(x.apply(null, args));
                    }
                }
                return stack;
            }

            var token:String, n:Number, op:Function;
            for each (token in StringUtil.trim(notation).split(/\s+/)){
                n = Number(token);
                if (isNaN(n)) {
                    op = Calc.operators[token];
                    if (op) {
                        commands.push(op);
                    } else {
                        commands.push(token);
                        addEventListener(token, function(e:Event):void {
                            view.apply(null, model().slice(0, view.length || 8));  // args max 8
                        });
                    }
                } else {
                    commands.push(n);
                }
            }
        }

    }
}

"""

if __name__ == "__main__":
    import re
    from tornado.template import Template

    s = Template(src).generate(
        attributes=sorted(attributes.items()),
        types=types,
        defaults=defaults,
        defines=defines,
    ).decode()
    print(re.sub(r'\s+\n+', '\n', s))
