def get_designs(cloth_type):

    designs = {

        "tshirt": [

            {
                "name": "Abstract Design 1",
                "image": "designs/abstract1.png"
            },

            {
                "name": "Abstract Design 2",
                "image": "designs/abstract2.png"
            },

            {
                "name": "Nature Design",
                "image": "designs/nature1.png"
            },

            {
                "name": "Spiral Design",
                "image": "designs/spiral1.png"
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
