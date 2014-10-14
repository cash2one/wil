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
            player:
                hpDelta: +1
                mpDelta: -1
                lvDelta: +1
                exp: 1234
        87:
            player:
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
    y: 235
    draggable: true
    hidden: true
    children:
        icon:
            x: 51
            y: 28
            lazy: true
        0:
            res: [-231, 231, 230]
            x: 299
            y: 83
            model: "switchFnTo"
            view: "fnRes2"
            events:
                click:
                    player:
                        switchFnTo: 0
        1:
            res: [-232, 232, 233]
            x: 34
            y: 83
            model: "switchFnTo"
            view: "fnRes2"
            events:
                click:
                    player:
                        switchFnTo: 1
        2:
            res: [-234, 234, 235]
            x: 66
            y: 83
            model: "switchFnTo"
            view: "fnRes2"
            events:
                click:
                    player:
                        switchFnTo: 2
        3:
            res: [-236, 236, 237]
            x: 98
            y: 83
            model: "switchFnTo"
            view: "fnRes2"
            events:
                click:
                    player:
                        switchFnTo: 3
        4:
            res: [-238, 238, 239]
            x: 130
            y: 83
            model: "switchFnTo"
            view: "fnRes2"
            events:
                click:
                    player:
                        switchFnTo: 4
        5:
            res: [-240, 240, 241]
            x: 171
            y: 83
            model: "switchFnTo"
            view: "fnRes2"
            events:
                click:
                    player:
                        switchFnTo: 5
        6:
            res: [-242, 242, 243]
            x: 203
            y: 83
            model: "switchFnTo"
            view: "fnRes2"
            events:
                click:
                    player:
                        switchFnTo: 6
        7:
            res: [-244, 244, 245]
            x: 235
            y: 83
            model: "switchFnTo"
            view: "fnRes2"
            events:
                click:
                    player:
                        switchFnTo: 7
        8:
            res: [-246, 246, 247]
            x: 267
            y: 83
            model: "switchFnTo"
            view: "fnRes2"
            events:
                click:
                    player:
                        switchFnTo: 8
        ok:
            res: [361, 362]
            x: 220
            y: 129
            events:
                click: "switchFnSubmit"





print = console.log.bind(console)
print(JSON.stringify(config))  # usage: ./ui.coffee >ui.json
# END
