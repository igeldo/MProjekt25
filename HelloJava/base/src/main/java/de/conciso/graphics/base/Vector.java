package de.conciso.graphics.base;

import java.util.Locale;

public class Vector extends Coordinate2D {

  public Vector(double x, double y) {
    super(x, y);
  }

  public String toString() {
    return String.format(Locale.ENGLISH, "Vector(%f, %f)", x, y);
  }

  public Vector add(Vector other) {
    return new Vector(x + other.x, y + other.y);
  }
}
