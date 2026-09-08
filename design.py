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
                "name": "Leaf Design",
                "image": "leaf/leaf.jpeg"
            },

            {
                "name": "Leaf Design",
                "image": "leaf/leaf2.jpeg"
                
            },

            {
                "name": "Line Design",
                "image": "line/line.jpeg"
            },

            {
                 "name": "Line Design",
                "image": "line/line2.jpeg"
                
            },
             {
                 "name": "Line Design",
                "image": "line/line3.jpeg"
                
            },
             {
                 "name": "Line Design",
                "image": "line/zigzag.jpeg"
                
            }

        ],

        "handkerchief": [

            {
                "name": "Spiral",
                "image": "spiral/s1.jpeg"
            },

            {
                "name": "Spiral",
                "image": "spiral/s2.jpeg"
                
            },

            {
                "name": "Spiral",
                "image": "spiral/s3.jpeg"
                
            },

            {
                "name": "Spiral",
                "image": "spiral/s4.jpeg"
                
            }

        ]

    }

    return designs.get(cloth_type, [])
