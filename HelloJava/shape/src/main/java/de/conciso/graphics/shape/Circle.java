package de.conciso.graphics.shape;

import de.conciso.graphics.base.Point;
import java.util.Locale;

public class Circle extends AbstractShape {

  private final double radius;

  public Circle(Point center, double radius) {
    super(center);
    if (radius<=0 ) {
      throw new IllegalArgumentException("Radius must be greater than 0");
    }
    this.radius = radius;
  }

  public double getRadius() {
    return radius;
  }

  @Override
  public double calculateArea() {
    return Math.PI * Math.pow(radius, 2);
  }

  public String toString() {
    return String.format(Locale.ENGLISH, "Circle(%s, %f)", center, radius);
  }
}
