package de.conciso.graphics.base;

import java.util.Objects;

public abstract class Coordinate2D {

  protected final double x;

  protected final double y;

  protected Coordinate2D(double x, double y) {
    this.x = x;
    this.y = y;
  }

  public double getY() {
    return y;
  }

  public double getX() {
    return x;
  }

  public abstract String toString();

  @Override
  public boolean equals(Object o) {
    if (this == o) return true;
    if (!(o instanceof Coordinate2D that)) return false;
    return Double.compare(x, that.x) == 0 && Double.compare(y, that.y) == 0;
  }

  @Override
  public int hashCode() {
    return Objects.hash(x, y);
  }
}
