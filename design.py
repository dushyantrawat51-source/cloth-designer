def get_designs(cloth_type):

    designs = {

        "tshirt": [

            {
                "name": "Rangoli",
                "image": "rangoli/r1.jpeg"
            },

            {
                 "name": "Rangoli",
                "image": "rangoli/r2.jpeg"
            },

            {
                 "name": "Rangoli",
                "image": "rangoli/r3.jpeg"
            },

            {
                 "name": "Rangoli",
                "image": "rangoli/r4.jpeg"
            },
            {
                 "name": "Rangoli",
                "image": "rangoli/r5.jpeg"
            },
            {
                 "name": "Floral Design",
                "image": "floral/Designe1.png"
            },
             {
                 "name": "Floral Design",
                "image": "floral/Designe2.png"
            },
             {
                 "name": "Floral Design",
                "image": "floral/Designe3.png"
            }

        ],

        "bedsheet": [

            {
                "name": "Floral Design 1",
                "image": "designs/floral1.png"
            },

            {
                "name": "Floral Design 2",
                "image": "designs/floral2.png"
            },

            {
                "name": "Mandala Design",
                "image": "designs/mandala1.png"
            },

            {
                "name": "Rangoli Design",
                "image": "designs/rangoli1.png"
            }

        ],

        "handkerchief": [

            {
                "name": "Flower Pattern 1",
                "image": "designs/floral1.png"
            },

            {
                "name": "Flower Pattern 2",
                "image": "designs/floral2.png"
            },

            {
                "name": "Flower Pattern 3",
                "image": "designs/floral3.png"
            },

            {
                "name": "Border Pattern",
                "image": "designs/border1.png"
            }

        ]

    }

    return designs.get(cloth_type, [])
