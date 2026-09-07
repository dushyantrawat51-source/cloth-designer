def get_designs(cloth_type):

    designs = {

        "tshirt": [
            {
                "name": "Abstract Design",
                "image":
                "https://images.unsplash.com/photo-1515886657613-9f3515b0c78f"
            },
            {
                "name": "Spiral Design",
                "image":
                "https://images.unsplash.com/photo-1517841905240-472988babdf9"
            },
            {
                "name": "Nature Design",
                "image":
                "https://images.unsplash.com/photo-1506744038136-46273834b3fb"
            }
        ],

        "bedsheet": [
            {
                "name": "Floral Design",
                "image":
                "https://images.unsplash.com/photo-1505693416388-ac5ce068fe85"
            },
            {
                "name": "Rangoli Design",
                "image":
                "https://images.unsplash.com/photo-1517694712202-14dd9538aa97"
            },
            {
                "name": "Mandala Pattern",
                "image":
                "https://images.unsplash.com/photo-1545239351-1141bd82e8a6"
            }
        ],

        "handkerchief": [
            {
                "name": "Flower Pattern1",
                "image":
                "https://designs/floral1.png"
            },
            {
                "name": "Flower Pattern2",
                "image":
                "https://designs/floral2.png"
            }
            {
                "name": "Flower Pattern3",
                "image":
                "https://designs/floral3.png"
            }
        ]
    }

    return designs.get(cloth_type, [])
