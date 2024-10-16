package de.conciso.graphics.base;

import static org.assertj.core.api.Assertions.assertThat;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class PointTest {

  Point cut;

  @BeforeEach
  void setUp() {
    cut = new Point(2, 3);
  }

  @Test
  void testToString() {
    // Act
    var result = cut.toString();

    // Assert
    assertThat(result).isEqualTo("Point(2.000000, 3.000000)");
  }

  @Test
  void testGetX() {
    // Act & Assert
    assertThat(cut.getX()).isEqualTo(2);
  }

  @Test
  void testGetY() {
    // Act & Assert
    assertThat(cut.getY()).isEqualTo(3);
  }

  @Test
  void testAdd() {
    // Arrange
    var other = new Vector(4, 5);
    var expected = new Point(6, 8);

    // Act
    var result = cut.add(other);

    // Assert
    assertThat(result).isEqualTo(expected);
  }
}
