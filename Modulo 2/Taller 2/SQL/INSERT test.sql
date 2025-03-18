-- INSERT GUARDERIAS
INSERT INTO TABLAS.GUARDERIAS (Nombre, Direccion, Telefono) VALUES
('La Favorita', 'Calle 123, Ciudad A', '1234567890'),
('Dog Haven', 'Avenida 456, Ciudad B', '9876543210'),
('Puppy Palace', 'Carrera 789, Ciudad C', '5551234567'),
('Canine Care', 'Calle 101, Ciudad D', '3334445555'),
('Pet Paradise', 'Avenida 202, Ciudad E', '6667778888');

-- INSERT CUIDADOR
INSERT INTO TABLAS.CUIDADOR (Nombre, Telefono, ID_GUARDERIA) VALUES
('Miguel', '1112223333', 1),
('Ana', '4445556666', 2),
('Luis', '7778889999', 3),
('Sofía', '1231231234', 4),
('Mario', '9879879876', 5);

-- INSERT PROPIETARIOS
INSERT INTO TABLAS.PROPIETARIOS (Nombre, Telefono) VALUES
('María', '9998887777'),
('Juan', '6665554444'),
('Elena', '3332221111'),
('Pedro', '1113335555'),
('Lucía', '4446668888');

-- INSERT PERRO
INSERT INTO TABLAS.PERRO (Nombre, Raza, Edad, Peso, ID_GUARDERIA, ID_CUIDADOR) VALUES
('Max', 'Labrador', 5, 25.50, 1, 1),
('Luna', 'Bulldog', 3, 18.20, 2, 2),
('Lassie', 'Pastor Alemán', 4, 30.00, 3, 3),
('Bella', 'Golden Retriever', 2, 22.80, 1, 1),
('Toby', 'Beagle', 6, 12.50, 2, 2),
('Milo', 'Poodle', 7, 9.30, 3, 3),
('Nala', 'Doberman', 3, 28.00, 4, 4),
('Simba', 'Husky', 4, 24.50, 5, 5),
('Lassie', 'Boxer', 5, 27.00, 1, 1),
('Daisy', 'Cocker Spaniel', 3, 13.80, 2, 2),
('Luna', 'Chihuahua', 2, 2.5, 3, 3),
('Max', 'Yorkshire Terrier', 3, 2.8, 4, 4),
('Bella', 'Pomerania', 1, 1.9, 5, 5),
('Rocky', 'Pinscher Miniatura', 4, 2.7, 1, 1),
('Coco', 'Caniche Toy', 2, 2.6, 3, 3);
