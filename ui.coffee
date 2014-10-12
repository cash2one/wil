#!/usr/bin/env coffee
config =

main:
    res: 1
    x: 0
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
            pages:
                hp:
                    pageIndex: 0
                    res: 5
                    children:
                        hpfull:
                            res: 6
                            model: "hp maxhp /"
                            view: "viewY"
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
                            view: "viewY"
                        mpfull:
                            res: 4
                            rectX: 0.5
                            rectW: 0.5
                            model: "mp maxmp /"
                            view: "viewY"
        lv:  #todo
            res: 30
            x: 665
            y: 147
        exp:
            res: 7
            x: 665
            y: 178
            model: "exp maxexp /"
            view: "viewW"
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
            view: "viewW"
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
            ox: "visible"
            page: "equipments"
        87:
            ox: "visible"
            page: "skills"
        69:
            ox: "visible"
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
                        click: "test"
                down:
                    res: [396, 397]
                    x: 175
                    y: 92
                    events:
                        doubleClick: "test"
                        rightClick: "test"
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




print = console.log.bind(console)
print(JSON.stringify(config))  # usage: ./ui.coffee >ui.json
# END
