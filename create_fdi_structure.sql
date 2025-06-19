-- Crear el tipo objeto para el FDI anual 

CREATE OR REPLACE TYPE fdi_anual_tipo AS OBJECT(
    anio NUMBER(4),
    fdi_porcentaje NUMBER(5,2)
    );
    
/

-- Crear el tipo tabla anidada para almacenar los FDI por año
CREATE OR REPLACE TYPE fdi_lista_tipo AS TABLE OF fdi_anual_tipo;
/
-- Crear la tabla principal con el país y su lista de FDI.
CREATE TABLE fdi_pais_objeto(
    nombre_pais VARCHAR2(100),
    codigo_pais VARCHAR(10),
    fdi_anual fdi_lista_tipo
)

NESTED TABLE fdi_anual STORE AS fdi_anual_nt;


-- Insertar datos en la tabla fdi_pais_objeto con listas anidadas
-- España
INSERT INTO fdi_pais_objeto VALUES (
    'España',
    'ESP',
    fdi_lista_tipo(
        fdi_anual_tipo(2000.0, 6.77), fdi_anual_tipo(2001.0, 4.6), fdi_anual_tipo(2002.0, 5.55),
        fdi_anual_tipo(2003.0, 3.39), fdi_anual_tipo(2004.0, 2.36), fdi_anual_tipo(2005.0, 2.34),
        fdi_anual_tipo(2006.0, 2.61), fdi_anual_tipo(2007.0, 4.62), fdi_anual_tipo(2008.0, 4.53),
        fdi_anual_tipo(2009.0, 0.64), fdi_anual_tipo(2010.0, 2.56), fdi_anual_tipo(2011.0, 1.8),
        fdi_anual_tipo(2012.0, 1.57), fdi_anual_tipo(2013.0, 3.46), fdi_anual_tipo(2014.0, 2.32),
        fdi_anual_tipo(2015.0, 1.97), fdi_anual_tipo(2016.0, 3.62), fdi_anual_tipo(2017.0, 2.54),
        fdi_anual_tipo(2018.0, 4.47), fdi_anual_tipo(2019.0, 2.16), fdi_anual_tipo(2020.0, 2.92),
        fdi_anual_tipo(2021.0, 4.42), fdi_anual_tipo(2022.0, 4.53)
    )
);

COMMIT;
-- Irlanda 
INSERT INTO fdi_pais_objeto VALUES (
    'Iralanda',
    'IRL',
    fdi_lista_tipo(
        fdi_anual_tipo(2000.0, 25.73), fdi_anual_tipo(2001.0, 8.83), fdi_anual_tipo(2002.0, 22.8),
        fdi_anual_tipo(2003.0, 13.83), fdi_anual_tipo(2004.0, -5.46), fdi_anual_tipo(2005.0, 22.18),
        fdi_anual_tipo(2006.0, 9.51), fdi_anual_tipo(2007.0, 22.19), fdi_anual_tipo(2008.0, 8.45),
        fdi_anual_tipo(2009.0, 22.83), fdi_anual_tipo(2010.0, 17.0), fdi_anual_tipo(2011.0, 9.82),
        fdi_anual_tipo(2012.0, 25.56), fdi_anual_tipo(2013.0, 29.81), fdi_anual_tipo(2014.0, 39.32),
        fdi_anual_tipo(2015.0, 74.75), fdi_anual_tipo(2016.0, 26.1), fdi_anual_tipo(2017.0, 20.41),
        fdi_anual_tipo(2018.0, 20.38), fdi_anual_tipo(2019.0, 7.68), fdi_anual_tipo(2020.0, 8.08),
        fdi_anual_tipo(2021.0, 14.63), fdi_anual_tipo(2022.0, -6.49)
    )
);

-- Unión Europea
INSERT INTO fdi_pais_objeto VALUES (
    'Unión Europea',
    'EUU',
    fdi_lista_tipo(
        fdi_anual_tipo(2000.0, 8.72), fdi_anual_tipo(2001.0, 4.96), fdi_anual_tipo(2002.0, 3.65),
        fdi_anual_tipo(2003.0, 2.95), fdi_anual_tipo(2004.0, 2.74), fdi_anual_tipo(2005.0, 6.12),
        fdi_anual_tipo(2006.0, 7.14), fdi_anual_tipo(2007.0, 9.99), fdi_anual_tipo(2008.0, 5.06),
        fdi_anual_tipo(2009.0, 3.96), fdi_anual_tipo(2010.0, 3.27), fdi_anual_tipo(2011.0, 5.68),
        fdi_anual_tipo(2012.0, 3.95), fdi_anual_tipo(2013.0, 3.89), fdi_anual_tipo(2014.0, 2.96),
        fdi_anual_tipo(2015.0, 6.23), fdi_anual_tipo(2016.0, 5.2), fdi_anual_tipo(2017.0, 3.97),
        fdi_anual_tipo(2018.0, 0.83), fdi_anual_tipo(2019.0, 3.69), fdi_anual_tipo(2020.0, 1.24),
        fdi_anual_tipo(2021.0, 3.76), fdi_anual_tipo(2022.0, 1.11)
    )
);
-- Estados Unidos
INSERT INTO fdi_pais_objeto VALUES (
    'Estados Unidos de América',
    'USA',
    fdi_lista_tipo(
        fdi_anual_tipo(2000.0, 3.41), fdi_anual_tipo(2001.0, 1.63), fdi_anual_tipo(2002.0, 1.02),
        fdi_anual_tipo(2003.0, 1.02), fdi_anual_tipo(2004.0, 1.75), fdi_anual_tipo(2005.0, 1.09),
        fdi_anual_tipo(2006.0, 2.16), fdi_anual_tipo(2007.0, 2.39), fdi_anual_tipo(2008.0, 2.31),
        fdi_anual_tipo(2009.0, 1.11), fdi_anual_tipo(2010.0, 1.75), fdi_anual_tipo(2011.0, 1.69),
        fdi_anual_tipo(2012.0, 1.54), fdi_anual_tipo(2013.0, 1.71), fdi_anual_tipo(2014.0, 1.43),
        fdi_anual_tipo(2015.0, 2.8), fdi_anual_tipo(2016.0, 2.52), fdi_anual_tipo(2017.0, 1.94),
        fdi_anual_tipo(2018.0, 1.04), fdi_anual_tipo(2019.0, 1.47), fdi_anual_tipo(2020.0, 0.64),
        fdi_anual_tipo(2021.0, 2.01),fdi_anual_tipo(2022.0, 1.57)
    )
);


SELECT * FROM fdi_pais_objeto