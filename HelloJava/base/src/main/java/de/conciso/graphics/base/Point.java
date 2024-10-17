package de.conciso.graphics.base;

import java.util.Locale;

public class Point extends Coordinate2D {

  public Point(double x, double y) {
    super(x, y);
  }

  public String toString() {
    return String.format(Locale.ENGLISH, "Point(%f, %f)", x, y);
  }

  public Point add(Vector other) {
    return new Point(x + other.getX(), y + other.getY());
  }
}
