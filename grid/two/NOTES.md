### [leccion 2](https://vimeo.com/717033709)

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
### leccion 3
- [codepen app 2 - layout real](https://codepen.io/diana_aceves/pen/QqMRmX/275d5969a7ac458d4b7cf27d516962db)
- [codepen - lineas nombradas](https://codepen.io/diana_aceves/pen/YrVxBa/932cd1f470414a8470f75ed1f7f2da97)
  - es como un layout tipico con su header, sidebar ,main y footer
```css

.grid {
    display: grid;
    grid-template-columns: repeat(6, 95px);
    grid-template-rows: repeat(6, 95px);
}
/*
podria colocar el item con una pseudo class nt-child
y seria lo mismo
.grid-item.nt-child(1) {

}
*/
.item1 {
    grid-column: span 3;
}
```
- lineas nombradas. 
- la ventaja de nombrar lineas es que actuan como variables y evitan que tengas que recolocar todo en la mediaquery.
si se hiciera con numeros habria que volver a indicar el inicio y fin
```css 
.grid{
  display: grid;
  grid-gap: .5rem;
  /*
  al mismo tiempo que marcamos los limites v y h se puede asignarles una etiqueta entre
  []
  */
  grid-template-columns: [start] minmax(200px, 20%) [main] 1fr [end];
  grid-template-rows:
      [header]
          minmax(4rem, auto)
      [main]
          300px
      [footer]
          minmax(4rem, auto)
      [end];
}

.header {
  //grid-column: span 3;
  grid-column: start/end;
}
.footer {
  /*la última linea tambien se puede instanciar con -1*/
  grid-column: start/end;
}
```
### [leccion 4](https://vimeo.com/719346964)
- lineas nombradas multiples
- [codepen - lineas nombradas multiples](https://codepen.io/diana_aceves/pen/VMbMpG/909b8f875ee1a123748330de23eacfa9?editors=0100)
```css
.grid {
  display: grid;
  grid-gap: .4rem;
  min-height: 100vh;
  grid-template-columns:
      [first nav-start] minmax(200px, 20%)
      [nav-end main-start] 1fr
      [main-end sidebar-start] minmax(200px, 20%)
      [sidebar-end last];

  grid-template-rows:
      [first header-start] minmax(4rem, auto)
      /*
      para que no haga scroll y se mantenga visible el footer como el header habria que
      incluir una altura fija en main y ponerle un overflow auto
      */
      [header-end main-start] 60vh
      [main-end footer-start] minmax(4rem, auto)
      [footer-end last];
}

/*
si deseo un header sticky ya no seria parte del grid, sino un elemento
externo flotante
*/
.header {
  grid-column: first / sidebar-start;
}
```
- lineas nombradas con variacion de numero de tracks
- [variacion de numero de tracks](https://codepen.io/diana_aceves/pen/dVWZYB/f69c230b24d46cfa9070955b295cc1fa?editors=0100)
  - permite agregar elementos al html sin tener que tocar practicamente el css
- [lineas nombradas con nombres repetidos](https://codepen.io/diana_aceves/pen/dVWmmP/4fb014e84bf66703d40aed25f38228e7?editors=0100)
  - permite agregar gaps virtuales y moverse sobre ellos
  ```css
  .grid {
    display: grid;
    grid-template-columns: [col] 10rem [gap] 1rem [col] 10rem [gap] 3rem [col] 1fr;
  }
  .item1 {
    /*
    le indico que comienze a dibujarse en la linea 3 que 
    coincide con el nombre col en segunda posicion
    */
    grid-column: col 2;
  }
  ```
- [areas nombradas](https://codepen.io/diana_aceves/pen/PJKGNp/c4e842619b3e9445a1aa6d4c7da14a8c)
- [Holy Grail Layout](https://codepen.io/diana_aceves/pen/d16c61719a681ceeb9d58ecf65271396?editors=0110)
```css
/*
a partir de 650px
*/
@media screen and (min-width: 650px) {
  //cambia config de filas,cols y areas
}
/*
a partir de 850
*/
@media screen and (min-width: 850px) {
  //cambia config de filas,cols y areas
}
```
- [Magic Lines - Areas - Lineas nombradas](https://codepen.io/diana_aceves/pen/RLZEBK/9bd610d26216beeb915de90af032f604?editors=0100)
```css
/*
uso nombres de lineas auto-generadas area-start y area-end
permite la superposición
Tambien se puede superponer en media celda, esto con
sidebar main
sidebar main
esto me crea dos celdas
y en overlap, uso el span
grid-row: header-start/3

*/
.overlap-item {
    background-color: rgba(0,255,0,.5);
    grid-row: header-end/footer-start;
    grid-column: sidebar-start/sidebar-end;
}
```
- [magic lines - lineas nombradas - areas](https://codepen.io/diana_aceves/pen/pWrmXg/d5686824a6b5af5a5f9592519cfe1076?editors=0100)
```css
/*
así como se pueden definir areas y estas auto-generan lineas start/end
se puede hacer a la invers, defino lineas xxx-start, xxx-end
y despues con estas puedo instanciar el area xxx
*/
.grid {
    display: grid;
    grid-gap: .5rem;
    grid-template-columns: repeat(2, 5rem)
        [main-start] repeat(2, 5rem)
        [main-end] repeat(2, 5rem)
    ;
    grid-template-rows: 5rem
        [main-start] repeat(2, 5rem)
        [main-end] 5rem
    ;
}
.item9 {
    background-color: salmon;
    grid-area: main;
}
```

- [Alineacion items](https://codepen.io/diana_aceves/pen/oGGwGP/47990d975d15d2ec00648c0ea5e08912)
- Un diseño irregular relaizado solo con posicionamientos x e y tanto de align como justify
```css
/*
alineacion en el eje Y:
    alignY-self
    alignY-items

alineacion en X:
    justifyX-self
    justifyX-items
*/
```
- [Alineacion tracks dentro del contenedor](https://codepen.io/diana_aceves/pen/BwwdGw/2c0cec9343124a9fc3eef11b1d5e9026)
- Esto crea espacios de manera uniforme
```css
.grid {
  /*
  valor por defecto
  */
  justify-content: start;
  justify-content: end;
  justify-content: center;
  justify-content: space-around;
  justify-content: space-between;
  /*
  todavia no a nivel de prod (comprobarlo)
  */
  justify-content: space-evenly;

  align-content: end;
  align-content: center;
  align-content: space-around;
  align-content: space-between;
  /*
  todavia no a nivel de prod (comprobarlo)
  */
  align-content: space-evenly;
}
```
- [EJ.10.1 - GRID-AUTO-FLOW: COLUMN](https://codepen.io/diana_aceves/pen/WZZXGb/7df12168a2abbaf64f629459176c1f23?editors=0100)
```css
.grid {
    display: grid;
    /*
    define la dirección en la que el grid va a crecer si necesita colocar items por auto-placement
    si pongo auto-flow column la idea es que yo controle el número de filas.
    En el ejemplo son 3 filas de 8 rem.
    A partir de este momento todos los items extra que agreguemos en el html iran creando columnas nuevas,
    es decir nuestro leyout crecera horizontalmnte
    */
    grid-auto-flow: column;
    grid-template-rows: repeat(3, 8rem);
}
```

### [leccion 5](https://vimeo.com/xxx)
- [EJ.10.2 - GRID-AUTO-FLOW: DENSE](https://codepen.io/diana_aceves/pen/JrrOea/38e47edb5e3fd08cb5f753e6e8df89f2)
```css
.item5 {
    /*
    como las columnas son fijas deja un hueco en su espacio
    y se mueve a la nueva fila y a partir de ahi coge 2 filas.
    Si por algún motivo el numero de span supera las columnas configuradas entonces si crea una nueva
    columna
    */
    grid-column: span 2;
    grid-row: span 2;
}

.item7 {
  /*
  video 19:53 puede que sea un bug de la especificacion. Al incluir este estilo, el item5 pierde
  su rowspan 2
  como no se puede expandir en esa fila hace un salto
  
  En 26:46 se corrige, no era un bug, es que no se habia especificado una altura para las filas (grid-auto-rows: 5rem;).
  Esto implicaba que si se generaban filas para los span row estas tuvieran un alto minimo.
  */
  grid-column: span 3;
  grid-row: span 3;
}
```
- [EJ.10.3 - ADIVINANDO QUÉ PASA](https://codepen.io/diana_aceves/pen/pWWpgd/c9c87f925d16d975632b21182811dd95)
```css
.item8 {
    /*como no puede buscar esta coord hacia atras la sig posicion libre es justo debajo del item7*/
    grid-column: 2 / span 2;
}
.item11 {
    /*
    como le forzamos la fila y la colum se posiciona, 8 que tambien estaba ahi, como ya no puede ocupera la col 2
    se mueve a la siguiente fila, el nueve no puede buscar espacios antes... solo despues del 8 luego el flujo restante
    se mantiene
    */
    grid-row: 4;
    grid-column: 1 /span 2;
}
```
- [INTRODUCCIÓN AUTO-PLACEMENT + GRID-ROW/COLUMN](https://codepen.io/diana_aceves/pen/xXXpzv/c0e2dcd0a72cf358331ec432f30b2da1?editors=0100)
```css
.b {
    grid-row-start: span 2;
    grid-row-end: span 2;
    grid-row: span 2;
    grid-row: auto / span 2;
    grid-row: span 2 / auto;
    /*
    esta forma es la más intuitiva pero no hace lo que debe, crea el span
    pero mueve b a l primera columna.
    Esto ocurre porque el eje principal no es auto. Es una cuestion del algoritmo de auto-placement
    */
    grid-row: 1/3;
    //grid-column: 2;

}

.a {
  /*
  el eje principal es row y no se ha tocado
  */
  grid-column: span 2;
}

.b {
  /*
  por mas que cambie el span no cambio su posicione en el eje principal.
  Esta sigue siendo auto, por lo tanto no cambia su posición
  */
  grid-row: span 2;
}

//otro ejemplo
.b {
//grid-row: span 2;

  /*
  con esta linea, forzamos que b se mueva a la col 1 y ocupe 3 teniendo
  mayor prioridad en el layout que A y haciendo que A se desplace hacia abajo
  */
  grid-row: 1/3;
}

.a {
  grid-column: 1/3;
}
```
[EJ.APLICACIÓN. 4 - TWO FULL COLUMNS](https://codepen.io/diana_aceves/pen/ZXaLGQ/4a474ea4cdc75fbfac33d340c950c2f7)
```css
.container {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    min-height: 100vh;
    padding: 1rem;
    grid-gap: 1rem;
}

.item {
    display: flex;
    align-items: center;
    justify-content: center;
}

.item--left {
    color: white;
    background-color: green;
}

.item--right {
    background-color: white;
}
.article__main {
    width: 60%;
    max-width: 350px;
}
.article__title {
    font-family: Serif;
    font-size: 2em;
}
.article__content {
    line-height: 1.3;
}
```
#### [Lección 6 última]()
- [EJ.APLICACIÓN. 5 - studiosouth.co.nz](https://codepen.io/diana_aceves/pen/pWdwQE/e59f03935ea7b5649eaf9a7a8616fffc)
```css
body {
    font-size: 1rem;
    font-family: 'Roboto', sans-serif;
    background-color: #2D2D2D;
    color: #ACB4B4;
}

/*
section.portfolio todo el grid
*/
.portfolio {
    padding: 10rem 5%;
    display: grid;
    /*
    no me respetaba el ancho pq no ponía una medida en px sino
    en 0.5fr
    */
    grid-template-columns: repeat(4, 1fr);
    grid-auto-rows: 190px;
    grid-column-gap: 1rem;
    grid-row-gap: 40px;
}

.portfolio .portfolio__item {
    /*
    se vera dentro del espacio del <article>
    */
    overflow: hidden;
}
/*article
    figcaption
    figure
*/
.portfolio figcaption {
    /*titulo Project - Edition*/
    height: 3rem;
    display: flex;
    /*
    alinea verticalmente el texto en
    la caja fcaption
    */
    align-items: center;
}

.portfolio figure {
    /*
    falta esto para que no se vea el "padding" al rededor de la imagen
    */
    margin:0;
    height: calc(100% - 3rem);
}

.portfolio figure img {
    height: 100%;
    width: 100%;
    /*
    hace que se ajuste por altura o anchura pero
    manteniendo su proporcion
    */
    object-fit: cover;
}

.item1, .item6, .item8 {
    grid-column: span 2;
    grid-row: span 2;
}

.item3, .item10 {
    grid-row: span 2;
}
.item4 {
    grid-column: 1;
    grid-row: span 2;
}
.item7 {
    grid-column: span 2;
    grid-row: span 2;
}
.header--main {
    position: fixed;
    width: 100%;
    height: 80px;
    background-color: #2D2D2D;
    padding: 0 5% 0 calc(5% - 1rem);
}
.header--main nav, ul {
    height: 100%;
}
/*
el ul es un grid
*/
.header--main ul{
    display: grid;
    grid-template-columns: repeat(4, minmax(180px, 1fr));
    align-items: center;
}

.header--main a {
    padding: 1rem;
}
```