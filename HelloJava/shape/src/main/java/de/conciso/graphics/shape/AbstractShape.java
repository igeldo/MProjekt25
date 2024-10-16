package de.conciso.graphics.shape;

import de.conciso.graphics.base.Point;

public abstract class AbstractShape implements Shape {

  protected final Point center;

  protected AbstractShape(Point center) {
    this.center = center;
  }

  public Point getCenter() {
    return center;
  }
}
