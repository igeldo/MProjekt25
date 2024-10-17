package de.conciso.graphics.shape;

import static org.assertj.core.api.Assertions.assertThat;
import static org.assertj.core.data.Percentage.withPercentage;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

import de.conciso.graphics.base.Point;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class CircleTest {

  Point center;
  Circle cut;

  @BeforeEach
  void setUp() {
    center = new Point(1, 2);
    cut = new Circle(center, 3);
  }

  @Test
  void testCreationFailsForNegativeRadius() {
    // Act & Assert
    assertThrows(IllegalArgumentException.class, () -> new Circle(center, -4));
  }

  @Test
  void testToString() {
    // Act
    var resut = cut.toString();

    // Assert
    assertThat(resut).isEqualTo("Circle(Point(1.000000, 2.000000), 3.000000)");
  }

  @Test
  void testGetCenter() {
    // Act & Assert
    assertThat(cut.getCenter()).isEqualTo(center);
  }

  @Test
  void testGetRadius() {
    // Act & Assert
    assertEquals(3, cut.getRadius());
  }

  @Test
  void testCalculateAreaUsingEqual() {
    // Act
    var result = cut.calculateArea();

    // Assert
    assertThat(result).isEqualTo(28.274333882308138);
  }

  @Test
  void testCalculateArea() {
    // Arrange
    var expected = 28.274;

    // Act
    var result = cut.calculateArea();

    // Assert
    assertThat(result).isCloseTo(expected, withPercentage(1));
  }
}
