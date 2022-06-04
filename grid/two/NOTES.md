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
```

