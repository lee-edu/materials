int WIDTH = 800;
int HEIGHT = 600;

void settings() {
  size(WIDTH, HEIGHT);
}

void setup() {
  background(255);
  fromSideMidpoints();
  fromCorners();
  fromCenter(); 
}

/** Generate n lines from (oX, oY) */
void generateNLines(int originX, int originY, int n) {
for (int i = 0; i < n; i++) {
line(originX, originY, random(WIDTH), random(HEIGHT));
  }
}

/** Generate n lines from the given origins */
void fromOrigins(int[][] origins, color c, int n) {
  stroke(c);
  for (int[] origin : origins) {
    generateNLines(origin[0], origin[1], n);
  }
}

/** Red lines from midpoints of four sides */
void fromSideMidpoints(){
int[][] midpoints = {{WIDTH/2, 0}, {WIDTH/2, HEIGHT}, {0, HEIGHT/2}, {WIDTH, HEIGHT/2}};
fromOrigins(midpoints, color(255,0,0,125), int(random(5,20)));
}

/** Blue lines from four corners */
void fromCorners() {
  stroke(0, 0, 255, 125);
  int[][] corners = {{0, 0} , {WIDTH, 0} , {0, HEIGHT} , {WIDTH, HEIGHT} };
  fromOrigins(corners, color(0,0,255,125), int(random(5,20)));
}

/** Yellow lines from the center */
void fromCenter() {
stroke(220, 210, 10);
generateNLines(WIDTH/2, HEIGHT/2, int(random(5, 20)));
}