#!/usr/bin/env python3

attributes = dict(
    name=str,
    hp=int,
    maxhp=int,
    mp=int,
    maxmp=int,
    exp=int,
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
    int: "Number",
    list: "Object",
    object: "Object",
    bool: "Boolean",
}

defaults = {
    str: "'???'",
    int: "0",
    list: "[]",
    object: "{}",
    bool: "false",
}

src = """
{% autoescape None %}
package mir  {
    import flash.events.Event;
    import flash.events.EventDispatcher;
    import mx.utils.StringUtil;

    public final class Player extends EventDispatcher {
        public static const _:Player = new Player();

        {% for a, t in attributes %}
        private var _{{ a }}:{{ types[t] }} = {{ defaults[t] }};
        public function get {{ a }}():{{ types[t] }} { return _{{ a }}; }
        public function set {{ a }}(_:{{ types[t] }}):void {
            {% if t in (list, object) %}
            for (var k:String in _) {
                _{{ a }}[k] = _[k];
            }
            {% else %}
            _{{ a }} = _;
            {% end %}
            dispatchEvent(new Event("_{{ a }}"));
        }
        {% end %}

        public function set ox(attr:String):void {
            this[attr] = !this[attr];
        }

        public function bindView(notation:String, view:Function):void {
            const self:Player = this;
            const commands:Array = [];

            function model():Array {
                /** copy from Calc.rpn */
                const stack:Array = [];
                var x:*, a:Number, b:Number;
                for each (x in commands){
                    if (x is Number) {
                        stack.push(x);
                    } else if (x is String) {
                        stack.push(self[x]);
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

            var cmd:String, n:Number, op:Function;
            for each (cmd in StringUtil.trim(notation).split(/\s+/)){
                n = Number(cmd);
                if (isNaN(n)) {
                    op = Calc.operators[cmd];
                    if (op) {
                        commands.push(op);
                    } else {
                        commands.push(cmd);
                        addEventListener("_" + cmd, function(e:Event):void {
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
    from tornado.template import Template
    with open("Player.as", "w") as f:
        f.write(Template(src).generate(
            attributes=sorted(attributes.items()),
            types=types,
            defaults=defaults,
        ).decode())
