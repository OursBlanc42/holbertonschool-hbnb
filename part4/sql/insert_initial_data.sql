-- Insert initial data

-- Insert administrator user
INSERT INTO users (id, first_name, last_name, email, password, is_admin)
VALUES (
    '36c9050e-ddd3-4c3b-9731-9f487208bbc1',
    'Admin',
    'airbnbear',
    'admin@example.com',
    '$2b$12$FKHyF05SBD9P.loYwka92ODRrbLvMcJhUnumfM7WOL.aM3tj89NCG', -- bcrypt hash of 'admin123'
    TRUE
);

-- Insert demo user John Doe and Jane Doe
INSERT INTO users (id, first_name, last_name, email, password, is_admin)
VALUES (
    'e4cb3ac8-3f11-4f9a-982e-1f6d17694c9f',
    'John',
    'Doe',
    'john@example.com',
    '$2b$12$L/OjQw6GnrHTb42CTC.hselZc686OW.FC.PdUhmyQJTIML4nIQSD.', -- bcrypt hash of 'azerty123'
    FALSE
),
(
    'a0d6479b-2b2e-4948-8b35-4e9ac5c3846a',
    'Jane',
    'Doe',
 'jane@example.com', 
    '$2b$12$pUPjGpjRIiYGfAia4Zltw.I9JdpJRSrT7mtxq879khj2oxco/FgkC', -- bcrypt hash of 'azerty123'
    FALSE
);


-- Insert demo places for John
-- John Place 1 : Beautiful villa House
INSERT INTO places (id, title, description, price, latitude, longitude, owner_id, created_at, updated_at)
VALUES
    (
        '884b6b34-5c63-47e8-ab60-a7ba6a63ddd1',
        'Beautiful villa house',
        'A lovely villa with a great view near Leffrinckoucke.',
        150.00,
        40.7128,
        -74.0060,
        'e4cb3ac8-3f11-4f9a-982e-1f6d17694c9f',
        CURRENT_TIMESTAMP,
        CURRENT_TIMESTAMP
    );

-- John Place 2 : Cozy Apartment 
INSERT INTO places (id, title, description, price, latitude, longitude, owner_id, created_at, updated_at)
VALUES
    (
        'cc09352c-31a5-43ec-8786-e17a36c2ac99',
        'Cozy apartment',
        'A cozy apartment in a quiet neighborhood.',
        100.00,
        51.5074,
        -0.1278,
        'e4cb3ac8-3f11-4f9a-982e-1f6d17694c9f',
        CURRENT_TIMESTAMP,
        CURRENT_TIMESTAMP
    );

-- John Place 3: Cheap bedroom 
INSERT INTO places (id, title, description, price, latitude, longitude, owner_id, created_at, updated_at)
VALUES
    (
        'a6061aab-736c-4194-8117-d4527e18795f',
        'Bedroom in my apartment',
        'I rent this bedroom in my cozy apartment in a quiet neighborhood.',
        10,
        51.5074,
        -0.1278,
        'e4cb3ac8-3f11-4f9a-982e-1f6d17694c9f',
        CURRENT_TIMESTAMP,
        CURRENT_TIMESTAMP
    );

-- Insert demo places for Jane
-- Jane Place 1: Modern Loft
INSERT INTO places (id, title, description, price, latitude, longitude, owner_id, created_at, updated_at)
VALUES
    (
        'd1e2f3g4-h5i6-j7k8-l9m0-n1o2p3q4r5s6',
        'Modern loft',
        'A stylish loft in the heart of the city.',
        200.00,
        34.0522,
        -118.2437,
        'a0d6479b-2b2e-4948-8b35-4e9ac5c3846a',
        CURRENT_TIMESTAMP,
        CURRENT_TIMESTAMP
    );

-- Jane Place 2: Rustic Cabin
INSERT INTO places (id, title, description, price, latitude, longitude, owner_id, created_at, updated_at)
VALUES
    (
        'e2f3g4h5-i6j7-k8l9-m0n1-o2p3q4r5s6t7',
        'Rustic cabin',
        'A cozy cabin in the woods with a fireplace.',
        100.00,
        44.4280,
        -110.5885,
        'a0d6479b-2b2e-4948-8b35-4e9ac5c3846a',
        CURRENT_TIMESTAMP,
        CURRENT_TIMESTAMP
    );

-- Jane Place 3: Beach House
INSERT INTO places (id, title, description, price, latitude, longitude, owner_id, created_at, updated_at)
VALUES
    (
        'f3g4h5i6-j7k8-l9m0-n1o2-p3q4r5s6t7u8',
        'Beach house',
        'A beautiful beach house with ocean views near Leffrinckoucke.',
        300.00,
        36.7783,
        -119.4179,
        'a0d6479b-2b2e-4948-8b35-4e9ac5c3846a',
        CURRENT_TIMESTAMP,
        CURRENT_TIMESTAMP
    );


-- Insert reviews for example data (John to Jane's place & Jane to John's place)
INSERT INTO reviews (id, text, rating, user_id, place_id)
VALUES
    (
        '7e2c42be-8936-4813-bba9-c623b8a98409',
        'This place is amazing! I had a great time and the service was excellent.',
        5,
        'e4cb3ac8-3f11-4f9a-982e-1f6d17694c9f',
        'd1e2f3g4-h5i6-j7k8-l9m0-n1o2p3q4r5s6'
    ),
    (
        '0e75219b-7a28-4326-a28f-357d40a1c9a4',
        'I really enjoyed my visit here. The atmosphere is perfect for a relaxing evening.',
        5,
        'a0d6479b-2b2e-4948-8b35-4e9ac5c3846a',
        '884b6b34-5c63-47e8-ab60-a7ba6a63ddd1'
    );


-- Insert initial amenities
INSERT INTO amenities (id, name)
VALUES
    ('a1b2c3d4-e5f6-7g8h-9i0j-k1l2m3n4o5p6', 'WiFi'),
    ('b2c3d4e5-f6g7-h8i9-j0k1-l2m3n4o5p6q7', 'Swimming Pool'),
    ('c3d4e5f6-g7h8-i9j0-k1l2-m3n4o5p6q7r8', 'Air Conditioning');
