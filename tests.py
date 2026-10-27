import unittest
import triangle
import circle
import square
import rectangle


class TriangleTestCase(unittest.TestCase):
   def test_triangle_area_zero(self):
       res = triangle.area(10.0, 0)
       self.assertEqual(round(res,6), round(0.0,6))
   def test_triangle_area_int(self):
       res = triangle.area(5, 10)
       self.assertEqual(round(res,6), round(25.0,6))
   def test_triangle_area_float(self):
       res = triangle.area(0.5, 10)
       self.assertEqual(round(res,6), round(2.5,6))
       
   def test_triangle_perimeter_zero(self):
       res = triangle.perimeter(0.0, 0.0, 0.0)
       self.assertEqual(round(res,6), round(0.0,6))
   def test_triangle_perimeter_int(self):
       res = triangle.perimeter(5, 10, 3)
       self.assertEqual(round(res,6), round(18.0,6))
   def test_triangle_perimeter_float(self):
       res = triangle.perimeter(0.5, 10.2, 13.3)
       self.assertEqual(round(res,6), round(24.0,6))
       
       
class CircleTestCase(unittest.TestCase):
   def test_circle_area_zero(self):
       res = circle.area(0.0)
       self.assertEqual(round(res,6), round(0.0,6))
   def test_circle_area_int(self):
       res = circle.area(5)
       self.assertEqual(round(res,6), round(78.539816,6))
   def test_circle_area_float(self):
       res = circle.area(2.3)
       self.assertEqual(round(res,6), round(16.619025,6))
       
   def test_circle_perimeter_zero(self):
       res = circle.perimeter(0.0)
       self.assertEqual(round(res,6), round(0.0,6))
   def test_circle_perimeter_int(self):
       res = circle.perimeter(5)
       self.assertEqual(round(res,6), round(31.415927,6))
   def test_circle_perimeter_float(self):
       res = circle.perimeter(3.3)
       self.assertEqual(round(res,6), round(20.734512,6))
       
       
class SquareTestCase(unittest.TestCase):
   def test_square_area_zero(self):
       res = square.area(0.0)
       self.assertEqual(round(res,6), round(0.0,6))
   def test_square_area_int(self):
       res = square.area(5)
       self.assertEqual(round(res,6), round(25.0,6))
   def test_square_area_float(self):
       res = square.area(0.5)
       self.assertEqual(round(res,6), round(0.25,6))
       
   def test_square_perimeter_zero(self):
       res = square.perimeter(0.0)
       self.assertEqual(round(res,6), round(0.0,6))
   def test_square_perimeter_int(self):
       res = square.perimeter(5)
       self.assertEqual(round(res,6), round(20.0,6))
   def test_square_perimeter_float(self):
       res = square.perimeter(0.5)
       self.assertEqual(round(res,6), round(2.0,6))
       
       
class RectangleTestCase(unittest.TestCase):
   def test_rectangle_area_zero(self):
       res = rectangle.area(10.0, 0)
       self.assertEqual(round(res,6), round(0.0,6))
   def test_rectangle_area_int(self):
       res = rectangle.area(5, 10)
       self.assertEqual(round(res,6), round(50.0,6))
   def test_rectangle_area_float(self):
       res = rectangle.area(0.5, 10)
       self.assertEqual(round(res,6), round(5.0,6))
       
   def test_rectangle_perimeter_zero(self):
       res = rectangle.perimeter(0.0, 0.0)
       self.assertEqual(round(res,6), round(0.0,6))
   def test_rectangle_perimeter_int(self):
       res = rectangle.perimeter(5, 10)
       self.assertEqual(round(res,6), round(30.0,6))
   def test_rectangle_perimeter_float(self):
       res = rectangle.perimeter(0.5, 10.2)
       self.assertEqual(round(res,6), round(21.4,6))
