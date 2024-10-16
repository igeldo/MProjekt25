package de.conciso.graphics.shape;

import de.conciso.graphics.base.Point;
import java.util.Locale;

public class Circle extends AbstractShape {

  private final double radius;

  public Circle(Point center, double radius) {
    super(center);
    this.radius = radius;
  }

  @Override
  public double calculateArea() {
    return Math.PI * Math.pow(radius, 2);
  }

  public String toString() {
    return String.format(Locale.ENGLISH, "Circle(%s, %f)", center, radius);
  }
}
