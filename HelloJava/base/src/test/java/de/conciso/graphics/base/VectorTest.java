package de.conciso.graphics.base;

import static org.assertj.core.api.Assertions.assertThat;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class VectorTest {

  Vector cut;

  @BeforeEach
  void setUp() {
    cut = new Vector(5, 6);
  }

  @Test
  void testToString() {
    // Act
    var result = cut.toString();

    // Assert
    assertThat(result).isEqualTo("Vector(5.000000, 6.000000)");
  }

  @Test
  void testAdd() {
    // Arrange
    var other = new Vector(4, 5);
    var expected = new Vector(9, 11);

    // Act
    var result = cut.add(other);

    // Assert
    assertThat(result).isEqualTo(expected);
  }

  @Test
  void testAddWithMock() {
    // Arrange
    var other = mock(Vector.class);
    when(other.getX()).thenReturn(4.0);
    when(other.getY()).thenReturn(5.0);
    var expected = new Vector(9, 11);

    // Act
    var result = cut.add(other);

    // Assert
    assertThat(result).isEqualTo(expected);
  }
}
