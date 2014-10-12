#!/usr/bin/env coffee
config =

main:
    resources: [1]
    x: 0
    y: 349
    transparent: true
    children:
        ball:
            resources: [-5]
            x: 38
            y: 90
            events:
                click:
                    main_ball:
                        pageDelta: +1
            pages:
                hp:
                    pageIndex: 0
                    resources: [5]
                    children:
                        hpfull:
                            resources: [6]
                            model: "hp maxhp /"
                            view: "viewY"
                hpmp:
                    pageIndex: 1
                    resources: [-4]
                    x: 2
                    y: 1
                    children:
                        hpfull:
                            resources: [4]
                            rectW: 0.5
                            model: "hp maxhp /"
                            view: "viewY"
                        mpfull:
                            resources: [4]
                            rectX: 0.5
                            rectW: 0.5
                            model: "mp maxmp /"
                            view: "viewY"
        lv:  #todo
            resources: [30]
            x: 665
            y: 147
        exp:
            resources: [7]
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
            resources: [7]
            x: 665
            y: 211
            model: "weight maxweight /"
            view: "viewW"
        equipsButton:
            resources: [-8, 8]
            x: 643
            y: 61
            events:
                click:
                    status:
                        ox: "visible"
                        page: "equipments"
        bagButton:
            resources: [-9, 9]
            x: 682
            y: 41
            events:
                click:
                    bag:
                        ox: "visible"
        skillsButton:
            resources: [-10, 10]
            x: 722
            y: 21
            events:
                click:
                    status:
                        ox: "visible"
                        page: "skills"
        soundButton:
            resources: [-11, 11]
            x: 764
            y: 11

bag:
    resources: [3]
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
            resources: [-371, 371]
            x: 309
            y: 203
            events:
                click:
                    bag:
                        visible: false
        use:
            resources: [-26, 26]
            x: 254
            y: 183
        gold:
            resources: [-27]
            x: 10
            y: 190
            events:
                click:  # test switch gold
                    bag_gold:
                        pageDelta: +1
            pages:
                gold1:
                    pageIndex: 0
                    resources: [27]
                gold2:
                    pageIndex: 1
                    resources: [28]
                gold3:
                    pageIndex: 2
                    resources: [29]

status:
    resources: [370]
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
            resources: [-371, 371]
            x: 8
            y: 39
            events:
                click:
                    status:
                        visible: false
        up:
            resources: [-373, 373]
            x: 7
            y: 128
            events:
                click:
                    status:
                        pageDelta: -1
        down:
            resources: [-372, 372]
            x: 7
            y: 187
            events:
                click:
                    status:
                        pageDelta: +1
    pages:
        points:
            pageIndex: 0
            resources: [-382]
            x: 38
            y: 52
        miscellaneous:
            pageIndex: 1
            resources: [382]
            x: 38
            y: 52
        skills:
            pageIndex: 2
            resources: [383]
            x: 38
            y: 52
            events:
                rightClick: "test"
            children:
                up:
                    resources: [398, 399]
                    x: 175
                    y: 62
                    events:
                        click: "test"
                down:
                    resources: [396, 397]
                    x: 175
                    y: 92
                    events:
                        doubleClick: "test"
                        rightClick: "test"
        equipments:
            pageIndex: 3
            resources: [-376]
            x: 38
            y: 52
            events:
                click:
                    status_pages_equipments:
                        pageDelta: +1
            pages:
                equipmentsM:
                    pageIndex: 0
                    resources: [376]
                equipmentsW:
                    pageIndex: 1
                    resources: [377]




print = console.log.bind(console)
print(JSON.stringify(config))  # usage: ./ui.coffee >ui.json
# END
