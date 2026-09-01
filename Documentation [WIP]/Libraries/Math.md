# 🧮 Math

The `Math` library provides a comprehensive suite of mathematical functions, trigonometric operations, and 2D vector structures. These functions are designed to intelligently evaluate statically in Python during compile-time if given constants, or dynamically generate optimized visual script nodes (like Taylor Series approximations or Newton-Raphson iterations) if given runtime variables.

```python
import PvzRH_node as pvn
from PvzRH_node.Math import Vector2, PI, HALF_PI
```

---

## 1. Constants

Predefined mathematical constants available for calculations.

| Constant | Value | Description |
| --- | --- | --- |
| `PI` | `3.14159265...` | Ratio of a circle's circumference to its diameter |
| `HALF_PI` | `1.57079632...` | Half the value of PI |
| `E` | `2.71828182...` | Base of the natural logarithm |
| `TAU` | `6.28318530...` | Ratio of a circle's circumference to its radius (2π) |
| `RAD2DEG` | `57.2957795...` | Conversion factor for Radians to Degrees |
| `DEG2RAD` | `0.01745329...` | Conversion factor for Degrees to Radians |
| `TWO_PI` | `6.28318530...` | 2 * PI (Equivalent to TAU) |

---

## 2. Common Math Functions

General-purpose mathematical and comparative functions.

### Basic Operations & Rounding

* **`abs(val)`**: Returns the absolute value of an integer or float.


* **`max(*args)` / `min(*args)**`: Returns the largest or smallest value from a sequence or multiple arguments.


* **`floor(value)`**: Returns the largest integer less than or equal to the value.


* **`ceil(value)`**: Returns the smallest integer greater than or equal to the value.


* **`round(value)`**: Rounds a value to the nearest integer.


* **`sign(value)`**: Returns `1` if positive, `-1` if negative, and `0` if zero.


* **`copy_sign(magnitude, sign)`**: Returns a value with the provided magnitude and the sign of the `sign` argument.



### Interpolation & Ranges

* **`clamp(value, min, max)`**: Restricts a value between a minimum and maximum bound.


* **`clamp01(value)`**: Restricts a value strictly between `0.0` and `1.0`.


* **`lerp(start, end, t)`**: Linearly interpolates between start and end by `t`, clamped to `[0, 1]`.


* **`lerp_unclamped(start, end, t)`**: Linearly interpolates without clamping `t`.



### Advanced Computation

* **`sqrt(val, precision=6)`**: Calculates the square root using Newton-Raphson iteration.


* **`cbrt(val, precision=6)`**: Calculates the cube root using Newton-Raphson iteration.


* **`natural_pow(base, exp)`**: Raises a base to a natural number exponent (must be >= 1).


* **`is_prime(val)`**: Evaluates primality. Generates an optimized $O(\sqrt{N})$ runtime loop if evaluated dynamically on the node canvas.



---

## 3. Trigonometry

Trigonometric functions handle angles in both radians and degrees. Dynamic runtime node evaluations use Taylor Series approximations and automatic range reduction wrapping for stability.

### Angle Utilities

* **`rad2deg(rad)`**: Converts radians to degrees.


* **`deg2rad(deg)`**: Converts degrees to radians.


* **`normalize_angle_360(angle)`**: Wraps a degree angle to the range `[0.0, 360.0)`.


* **`normalize_angle_180(angle)`**: Wraps a degree angle to the range `[-180.0, 180.0)`.


* **`delta_angle(current, target)`**: Calculates the shortest rotational difference between two angles.


* **`lerp_angle(a, b, t)`**: Linearly interpolates taking the shortest rotational path.



### Standard & Inverse Trig

* **Functions**: `sin(rad)`, `cos(rad)`, `tan(rad)`, `cosec(rad)`, `sec(rad)`, `cot(rad)`.


* **Inverse**: `asin(val)`, `acos(val)`, `atan(val)`, `acosec(val)`, `asec(val)`, `acot(val)`.



(Note: All dynamic trigonometric functions accept a `terms` parameter to control the Taylor Series approximation precision, defaulting to 5).

---

## 4. Procedural Generation

### `perlin_noise(x, y)`

Calculates 2D Gradient Perlin Noise normalized strictly to a `[0.0, 1.0]` output range.

* **Static Evaluation**: Uses a quintic polynomial fade curve and high-entropy integer hashing via XOR bit-mixing.


* **Dynamic Node Evaluation**: Falls back to smoothstep interpolations and coordinate hashing via native math nodes.



```python
with pvn.Trigger.OnWave():
    # Use Perlin noise to smoothly vary zombie spawn columns based on the wave index
    noise_val = pvn.Math.perlin_noise(pvn.Board.Wave * 0.5, 0.0)
    spawn_col = pvn.Math.lerp(5.0, 9.0, noise_val)
    
    pvn.Spawner.Set_Zombie(row=2, col=spawn_col, zombie_type=pvn.ZombieType.Zombie)
```

---

## 5. 2D Vectors (`Vector2`)

The `Vector2` class wraps numerical coordinates or dynamic execution port variables for 2D spatial math.

### Initialization & Factories

```python
# Create a specific vector
pos = Vector2(4.0, 5.0)

# Built-in directional factories
zero_vec = Vector2.zero()   # (0.0, 0.0)
up_vec = Vector2.up()       # (0.0, 1.0)
right_vec = Vector2.right() # (1.0, 0.0)
```

### Vector Operations

Native Python operators (`+`, `-`, `*`, `/`, `==`, `-v`) are fully overloaded to support both component-wise vector math and scalar math.

```python
v1 = Vector2(2.0, 3.0)
v2 = Vector2(1.0, 1.0)

# Operator Overloading
v3 = v1 + v2        # Vector2(3.0, 4.0)
v4 = v1 * 2.0       # Vector2(4.0, 6.0) - Scalar multiplication
v5 = -v1            # Vector2(-2.0, -3.0) - Negation
```

### Methods

| Method | Description |
| --- | --- |
| `.magnitude()` | Returns the actual length of the vector |
| `.sqr_magnitude()` | Returns the squared length (`x^2 + y^2`), faster than `.magnitude()`<br> |
| `.normalized()` | Returns a scaled vector with a magnitude of `1.0`<br> |
| `Vector2.dot(v1, v2)` | Calculates the dot product of two vectors |
| `Vector2.distance(v1, v2)` | Calculates the exact Euclidean distance between two vectors |
| `Vector2.lerp(v1, v2, t)` | Interpolates between two vectors by `t`<br> |
| `.to_string()` | Formats the vector as `(x, y)` natively on the visual canvas |
