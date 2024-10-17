package de.conciso.graphics.app;

import de.conciso.graphics.base.Point;
import de.conciso.graphics.shape.Circle;
import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;

public class Main implements Runnable {

  private final static Logger log = LogManager.getLogger(Main.class);

  public void run() {
    var circle = new Circle(new Point(12.5, 14), 3);
    log.info(String.format("%s has area: %f", circle, circle.calculateArea()));
  }

  public static void main(String[] args) {
    var main = new Main();
    main.run();
  }
}
