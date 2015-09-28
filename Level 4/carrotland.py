from fractions import gcd

def CrossProduct(vecA, vecB):
	return vecA[0] * vecB[1] - vecA[1] * vecB[0]

def VectorSubtraction(vecA, vecB):
	return map(lambda p : p[0] - p[1], zip(vecA, vecB))

def NumPointsOnSegment(pointA, pointB):
	return gcd(abs(pointA[0] - pointB[0]), abs(pointA[1] - pointB[1])) + 1

def DoubleTriangleArea(vertices):
	return abs(CrossProduct(VectorSubtraction(vertices[1], vertices[0]), VectorSubtraction(vertices[2], vertices[0])))

def answer(vertices):
	return (DoubleTriangleArea(vertices) - NumPointsOnSegment(vertices[0], vertices[1]) - NumPointsOnSegment(vertices[1], vertices[2]) - NumPointsOnSegment(vertices[0], vertices[2]) + 3) / 2 + 1