### leccion 2
```css
.grid {
display: grid;
grid-gap: .5rem;
/*
autofill indica el autocalculo que caben. Yo le doy el min y el max y el autofill
ya se encarga de calcular las que se pueden incluir
solo se puede usar autofill/fit 1 vez en un solo repeat

repite por todo el ancho con columnas de 15rem mientras quepan sino haz un salto de linea
todavia no es responsive pq deja un hueco en el salto de linea
*/
//grid-template-columns: repeat(auto-fill, 15rem);

/*
esto si es responsive, el ancho q tengo entre 10rem = x columnas
*/
//grid-template-columns: repeat(auto-fill, minmax(10rem, 1fr));

//grid-template-columns: repeat(auto-fill, 20% minmax(10rem, 1fr));

/*
esto no tiraria: repeat(auto-fill, 20% 1fr) ya que el fr debe estar en un minmax
si en minmax(autofill, 120px, 250px) siempre se crearan de 250px es decir solo funciona con fr o porcentaje

columnas: 8rem-x, 8rem-x, 15rem-x * n hasta que ocupe el resto de espacio
*/
//grid-template-columns: repeat(2, minmax(8rem, 1fr)) repeat(auto-fill, minmax(15rem, 2fr));

//grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));

/*
auto-fit estira los elementos para que no queden huecos si sobra espacio.
auto-fill (crea espacios) estira los elementos crea esos si faltan celdas
*/

/*
con esto forzamos que en el espacio en la fila quepa el pack entero 150 + 300
*/
//grid-template-columns: repeat(auto-fill, 150px 300px);

//grid-template-columns: repeat(auto-fill, 150px minmax(100px, 1fr));

/*
3 columnas 1fr
*/
grid-template-columns: repeat(3, 1fr);

/*
dos filas de 5rem - infinito
*/
grid-template-rows: repeat(2, minmax(5rem, auto));

/*
nuevas filas 5rem - infinito (56:22), no se ha conseguido hacer crecer automaticamente hasta el infinito
la fila. Lo contará en el sig viedeo
*/
grid-auto-rows: minmax(5rem, 1fr);
}

.item1 {
/*
las coords empiezan por 1 tanto para x como para y
coord eje x (lin vert 1 hata lin vert 3)
*/
grid-column-start: 2;
grid-column-end: 3;

/*
coord y (lin hor 2 hasta lin hot 3)
*/
grid-row-start: 2;
grid-row-end: 3;

/*
en este caso le digo mantente en la h-lin 1 pero expandete a la v-lin 2
*/
//grid-column: span 2;
/*
empieza en v:2 y expandete 2
empieza en h:3 y expandete 3
*/
grid-column: 2 /span 2;
grid-row: 3/span 3;
}

.item1 {
/*
en caso que le pase más columnas de las q existan se fuerza la creacion de cols
*/
grid-column: 2/span 3;
grid-row: 1/3;

/*
grid-column y grid-row configuran una area. Esta area se puede configurar

el equivalente row-start/col-start/row-end/col-end
*/
grid-area: 1/2/3/span 3;
}

/*
si las coord de las areas se solapan entonces se superponen
*/
.item6 {
/*
en caso que le pase más columnas de las q existan se fuerza la creacion de cols
*/
grid-row: 3/7;
}

/*
superposicion de areas
*/
.grid {
display: grid;
grid-gap: .5rem;
grid-template-columns: repeat(3, 1fr);
grid-auto-columns: 1fr;
grid-auto-rows: 5rem;
}

.grid-item.item1 {
grid-column: 2/span 3;
grid-row: 1/3;
background-color: rgba(255,0,0,.5);
}

.grid-item.item6 {
grid-column: 2/span 3;
grid-row: 1/3;
background-color: rgba(0,255,0,.2);
}

/*
sistema de 12 columnas
*/
.grid {
    display: grid;
    grid-gap: .5rem;
    grid-template-columns: repeat(12, 1fr);
}
/*
escoge los elementos (con el selector .grid-item) localizados entre la
pos 13 y 18 incluidos
...
*/
.grid-item:nth-child(n+13):nth-child(-n+18) {
    grid-column: span 2;
}

.grid-item:nth-child(n+19):nth-child(-n+22) {
    grid-column: span 3;
}

.grid-item:nth-child(n+23):nth-child(-n+25) {
    grid-column: span 4;
}

.grid-item:nth-child(n+26):nth-child(-n+27) {
    grid-column: span 6;
}

.grid-item:nth-child(28) {
    grid-column: span 12;
}
```

