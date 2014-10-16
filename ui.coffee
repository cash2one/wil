#!/usr/bin/env coffee
config =

main:
    res: 1
    y: 349
    transparent: true
    children:
        ball:
            res: -5
            x: 38
            y: 90
            events:
                click:
                    main_ball:
                        pageDelta: +1
            children:
                hpmp:
                    y: 100
                    text: "HP:{0} MP:{1}"
                    model: "hp mp"
            pages:
                hp:
                    pageIndex: 0
                    res: 5
                    children:
                        hpfull:
                            res: 6
                            model: "hp maxhp /"
                            view: "y"
                hpmp:
                    pageIndex: 1
                    res: -4
                    x: 2
                    y: 1
                    children:
                        hpfull:
                            res: 4
                            rectW: 0.5
                            model: "hp maxhp /"
                            view: "y"
                        mpfull:
                            res: 4
                            rectX: 0.5
                            rectW: 0.5
                            model: "mp maxmp /"
                            view: "y"
        lv:
            x: 666
            y: 147
            model: "lv"
            view: "digit"
            children:
                0:
                    res: [30,31,32,33,34,35,36,37,38,39]
                1:
                    x: 8
                    res: [30,31,32,33,34,35,36,37,38,39]
                2:
                    x: 16
                    res: [30,31,32,33,34,35,36,37,38,39]
        exp:
            res: 7
            x: 665
            y: 178
            model: "exp maxexp /"
            view: "w"
            events:
                mouseOver:
                    exp_txt:
                        visible: true
                mouseOut:
                    exp_txt:
                        visible: false
        weight:
            res: 7
            x: 665
            y: 211
            model: "weight maxweight /"
            view: "w"
        equipsButton:
            res: [-8, 8]
            x: 643
            y: 61
            events:
                click:
                    status:
                        ox: "visible"
                        page: "equipments"
        bagButton:
            res: [-9, 9]
            x: 682
            y: 41
            events:
                click:
                    bag:
                        ox: "visible"
        skillsButton:
            res: [-10, 10]
            x: 722
            y: 21
            events:
                click:
                    status:
                        ox: "visible"
                        page: "skills"
        soundButton:
            res: [-11, 11]
            x: 764
            y: 11
            events:
                click:
                    npc:
                        visible: true
                    npc_buy:
                        visible: true
                    npc_sell:
                        visible: true
                    bag:
                        x: 400
                        y: 64

bag:
    res: 3
    x: 20
    y: 20
    transparent: true
    hidden: true
    draggable: true
    hotkeys:
        65:
            ox: "visible"
    children:
        close:
            res: [-371, 371]
            x: 309
            y: 203
            events:
                click:
                    bag:
                        visible: false
        use:
            res: [-26, 26]
            x: 254
            y: 183
        gold:
            res: -27
            x: 10
            y: 190
            events:
                click:  # test switch gold
                    bag_gold:
                        pageDelta: +1
            pages:
                gold1:
                    pageIndex: 0
                    res: 27
                gold2:
                    pageIndex: 1
                    res: 28
                gold3:
                    pageIndex: 2
                    res: 29

status:
    res: 370
    x: 565
    y: 10
    transparent: true
    hidden: true
    draggable: true
    hotkeys:
        81:
            P:
                hpDelta: +1
                mpDelta: -1
                lvDelta: +1
                exp: 1234
                shoplist: []
        87:
            P:
                hpDelta: -1
                mpDelta: +1
        69:
            ox: "visible"
            page: "skills"
    children:
        close:
            res: [-371, 371]
            x: 8
            y: 39
            events:
                click:
                    status:
                        visible: false
        up:
            res: [-373, 373]
            x: 7
            y: 128
            events:
                click:
                    status:
                        pageDelta: -1
        down:
            res: [-372, 372]
            x: 7
            y: 187
            events:
                click:
                    status:
                        pageDelta: +1
    pages:
        points:
            pageIndex: 0
            res: -382
            x: 38
            y: 52
        miscellaneous:
            pageIndex: 1
            res: 382
            x: 38
            y: 52
        skills:
            pageIndex: 2
            res: 383
            x: 38
            y: 52
            events:
                rightClick: "test"
            children:
                up:
                    res: [398, 399]
                    x: 175
                    y: 62
                    events:
                        click:
                            status_pages_skills:
                                pageDelta: -1
                down:
                    res: [396, 397]
                    x: 175
                    y: 92
                    events:
                        click:
                            status_pages_skills:
                                pageDelta: +1
        equipments:
            pageIndex: 3
            res: -376
            x: 38
            y: 52
            events:
                click:
                    status_pages_equipments:
                        pageDelta: +1
            pages:
                equipmentsM:
                    pageIndex: 0
                    res: 376
                equipmentsW:
                    pageIndex: 1
                    res: 377

switchFn:
    res: 229
    x: 212
    y: 220
    hidden: true
    events:
        click: "highlightFn"
    children:
        icon:
            x: 51
            y: 28
            lazy: true
        0:
            res: [-231, 231, 230]
            x: 299
            y: 83
        1:
            res: [-232, 232, 233]
            x: 34
            y: 83
        2:
            res: [-234, 234, 235]
            x: 66
            y: 83
        3:
            res: [-236, 236, 237]
            x: 98
            y: 83
        4:
            res: [-238, 238, 239]
            x: 130
            y: 83
        5:
            res: [-240, 240, 241]
            x: 171
            y: 83
        6:
            res: [-242, 242, 243]
            x: 203
            y: 83
        7:
            res: [-244, 244, 245]
            x: 235
            y: 83
        8:
            res: [-246, 246, 247]
            x: 267
            y: 83
        ok:
            res: [361, 362]
            x: 220
            y: 129
            events:
                click: "switchFnSubmit"

npc:
    res: 384
    hidden: true
    children:
        close:
            x: 399
            y: 1
            res: [-371, 371]
            events:
                click:
                    npc:
                        visible: false
        buy:
            res: 385
            y: 176
            events:
                mouseOut:
                    npc_buy_detail:
                        visible: false
            children:
                close:
                    res: [-371, 371]
                    x: 291
                    events:
                        click:
                            npc_buy:
                                visible: false
                ok:
                    res: [-386, 386]
                    x: 215
                    y: 171
                left:
                    x: 43
                    y: 175
                    res: [-388, 388]
                right:
                    x: 90
                    y: 175
                    res: [-387, 387]
                head:
                    x: 20
                    y: 9
                    text: "物品列表            价格         持久"
                detail:
                    x: 293
                    children:
                        0:
                            text: "{0}"
                        1:
                            y: 13
                            text: "{0}"
                        2:
                            y: 26
                            text: "{0}"
                        3:
                            y: 39
                            text: "{0}"
                0:
                    y: 29
                    events:
                        click: "shopSelect"
                    children:
                        name:
                            x: 20
                            text: "{0}"
                            model: "shoplist.0.1"
                        gold:
                            x: 155
                            text: "{0}"
                            model: "shoplist.0.2"
                        durability:
                            x: 245
                            text: "{0}"
                            model: "shoplist.0.3"
                1:
                    y: 42
                    events:
                        click: "shopSelect"
                    children:
                        name:
                            x: 20
                            text: "{0}"
                            model: "shoplist.1.1"
                        gold:
                            x: 155
                            text: "{0}"
                            model: "shoplist.1.2"
                        durability:
                            x: 245
                            text: "{0}"
                            model: "shoplist.1.3"
                2:
                    y: 55
                    events:
                        click: "shopSelect"
                    children:
                        name:
                            x: 20
                            text: "{0}"
                            model: "shoplist.2.1"
                        gold:
                            x: 155
                            text: "{0}"
                            model: "shoplist.2.2"
                        durability:
                            x: 245
                            text: "{0}"
                            model: "shoplist.2.3"
                3:
                    y: 68
                    events:
                        click: "shopSelect"
                    children:
                        name:
                            x: 20
                            text: "{0}"
                            model: "shoplist.3.1"
                        gold:
                            x: 155
                            text: "{0}"
                            model: "shoplist.3.2"
                        durability:
                            x: 245
                            text: "{0}"
                            model: "shoplist.3.3"
                4:
                    y: 81
                    events:
                        click: "shopSelect"
                    children:
                        name:
                            x: 20
                            text: "{0}"
                            model: "shoplist.4.1"
                        gold:
                            x: 155
                            text: "{0}"
                            model: "shoplist.4.2"
                        durability:
                            x: 245
                            text: "{0}"
                            model: "shoplist.4.3"
                5:
                    y: 94
                    events:
                        click: "shopSelect"
                    children:
                        name:
                            x: 20
                            text: "{0}"
                            model: "shoplist.5.1"
                        gold:
                            x: 155
                            text: "{0}"
                            model: "shoplist.5.2"
                        durability:
                            x: 245
                            text: "{0}"
                            model: "shoplist.5.3"
                6:
                    y: 107
                    events:
                        click: "shopSelect"
                    children:
                        name:
                            x: 20
                            text: "{0}"
                            model: "shoplist.6.1"
                        gold:
                            x: 155
                            text: "{0}"
                            model: "shoplist.6.2"
                        durability:
                            x: 245
                            text: "{0}"
                            model: "shoplist.6.3"
                7:
                    y: 120
                    events:
                        click: "shopSelect"
                    children:
                        name:
                            x: 20
                            text: "{0}"
                            model: "shoplist.7.1"
                        gold:
                            x: 155
                            text: "{0}"
                            model: "shoplist.7.2"
                        durability:
                            x: 245
                            text: "{0}"
                            model: "shoplist.7.3"
                8:
                    y: 133
                    events:
                        click: "shopSelect"
                    children:
                        name:
                            x: 20
                            text: "{0}"
                            model: "shoplist.8.1"
                        gold:
                            x: 155
                            text: "{0}"
                            model: "shoplist.8.2"
                        durability:
                            x: 245
                            text: "{0}"
                            model: "shoplist.8.3"
                9:
                    y: 146
                    events:
                        click: "shopSelect"
                    children:
                        name:
                            x: 20
                            text: "{0}"
                            model: "shoplist.9.1"
                        gold:
                            x: 155
                            text: "{0}"
                            model: "shoplist.9.2"
                        durability:
                            x: 245
                            text: "{0}"
                            model: "shoplist.9.3"
        sell:
            res: 392
            x: 260
            y: 176
            #hidden: true
            children:
                close:
                    res: [-371, 371]
                    x: 115
                    events:
                        click:
                            npc_sell:
                                visible: false
                ok:
                    res: [-393, 393]
                    x: 85
                    y: 150
                    events:
                        click: "sell"
                gold:
                    x: 4
                    y: 4
                    text: "{0}"






print = console.log.bind(console)
print(JSON.stringify(config))  # usage: ./ui.coffee >ui.json
# END
