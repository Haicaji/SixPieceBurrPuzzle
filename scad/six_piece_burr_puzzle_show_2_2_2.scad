// SCAD file for Six Piece Burr Puzzle
// 整体模型
union() {
  translate([5, 5, 0]) color([1, 0.8, 0, 0.85]) cube([5, 5, 5]);
  translate([10, 5, 0]) color([1, 0.8, 0, 0.85]) cube([5, 5, 5]);
  translate([5, 10, 0]) color([1, 0.8, 0, 0.85]) cube([5, 5, 5]);
  translate([10, 10, 0]) color([1, 0.8, 0, 0.85]) cube([5, 5, 5]);
  translate([5, 0, 5]) color([0, 0.8, 0, 0.85]) cube([5, 5, 5]);
  translate([10, 0, 5]) color([0, 0.8, 0, 0.85]) cube([5, 5, 5]);
  translate([0, 5, 5]) color([0.6, 0, 1, 0.85]) cube([5, 5, 5]);
  translate([5, 5, 5]) color([0.8, 0.8, 0.8, 0.85]) cube([5, 5, 5]);
  translate([10, 5, 5]) color([0.8, 0.8, 0.8, 0.85]) cube([5, 5, 5]);
  translate([15, 5, 5]) color([1, 0.4, 0, 0.85]) cube([5, 5, 5]);
  translate([0, 10, 5]) color([0.6, 0, 1, 0.85]) cube([5, 5, 5]);
  translate([5, 10, 5]) color([0.8, 0.8, 0.8, 0.85]) cube([5, 5, 5]);
  translate([10, 10, 5]) color([0.8, 0.8, 0.8, 0.85]) cube([5, 5, 5]);
  translate([15, 10, 5]) color([1, 0.4, 0, 0.85]) cube([5, 5, 5]);
  translate([5, 15, 5]) color([1, 0, 0, 0.85]) cube([5, 5, 5]);
  translate([10, 15, 5]) color([1, 0, 0, 0.85]) cube([5, 5, 5]);
  translate([5, 0, 10]) color([0, 0.8, 0, 0.85]) cube([5, 5, 5]);
  translate([10, 0, 10]) color([0, 0.8, 0, 0.85]) cube([5, 5, 5]);
  translate([0, 5, 10]) color([0.6, 0, 1, 0.85]) cube([5, 5, 5]);
  translate([5, 5, 10]) color([0.8, 0.8, 0.8, 0.85]) cube([5, 5, 5]);
  translate([10, 5, 10]) color([0.8, 0.8, 0.8, 0.85]) cube([5, 5, 5]);
  translate([15, 5, 10]) color([1, 0.4, 0, 0.85]) cube([5, 5, 5]);
  translate([0, 10, 10]) color([0.6, 0, 1, 0.85]) cube([5, 5, 5]);
  translate([5, 10, 10]) color([0.8, 0.8, 0.8, 0.85]) cube([5, 5, 5]);
  translate([10, 10, 10]) color([0.8, 0.8, 0.8, 0.85]) cube([5, 5, 5]);
  translate([15, 10, 10]) color([1, 0.4, 0, 0.85]) cube([5, 5, 5]);
  translate([5, 15, 10]) color([1, 0, 0, 0.85]) cube([5, 5, 5]);
  translate([10, 15, 10]) color([1, 0, 0, 0.85]) cube([5, 5, 5]);
  translate([5, 5, 15]) color([0, 0.4, 1, 0.85]) cube([5, 5, 5]);
  translate([10, 5, 15]) color([0, 0.4, 1, 0.85]) cube([5, 5, 5]);
  translate([5, 10, 15]) color([0, 0.4, 1, 0.85]) cube([5, 5, 5]);
  translate([10, 10, 15]) color([0, 0.4, 1, 0.85]) cube([5, 5, 5]);
}

// 零件 D
union() {
  translate([5.0, 5.0, -30.0]) color([1, 0.8, 0, 0.85]) cube([5, 5, 5]);
  translate([10.0, 5.0, -30.0]) color([1, 0.8, 0, 0.85]) cube([5, 5, 5]);
  translate([5.0, 10.0, -30.0]) color([1, 0.8, 0, 0.85]) cube([5, 5, 5]);
  translate([10.0, 10.0, -30.0]) color([1, 0.8, 0, 0.85]) cube([5, 5, 5]);
}

// 零件 B
union() {
  translate([5.0, -30.0, 5.0]) color([0, 0.8, 0, 0.85]) cube([5, 5, 5]);
  translate([10.0, -30.0, 5.0]) color([0, 0.8, 0, 0.85]) cube([5, 5, 5]);
  translate([5.0, -30.0, 10.0]) color([0, 0.8, 0, 0.85]) cube([5, 5, 5]);
  translate([10.0, -30.0, 10.0]) color([0, 0.8, 0, 0.85]) cube([5, 5, 5]);
}

// 零件 F
union() {
  translate([-30.0, 5.0, 5.0]) color([0.6, 0, 1, 0.85]) cube([5, 5, 5]);
  translate([-30.0, 10.0, 5.0]) color([0.6, 0, 1, 0.85]) cube([5, 5, 5]);
  translate([-30.0, 5.0, 10.0]) color([0.6, 0, 1, 0.85]) cube([5, 5, 5]);
  translate([-30.0, 10.0, 10.0]) color([0.6, 0, 1, 0.85]) cube([5, 5, 5]);
}

// 零件 public
union() {
  translate([35.0, 35.0, 35.0]) color([0.8, 0.8, 0.8, 0.85]) cube([5, 5, 5]);
  translate([40.0, 35.0, 35.0]) color([0.8, 0.8, 0.8, 0.85]) cube([5, 5, 5]);
  translate([35.0, 40.0, 35.0]) color([0.8, 0.8, 0.8, 0.85]) cube([5, 5, 5]);
  translate([40.0, 40.0, 35.0]) color([0.8, 0.8, 0.8, 0.85]) cube([5, 5, 5]);
  translate([35.0, 35.0, 40.0]) color([0.8, 0.8, 0.8, 0.85]) cube([5, 5, 5]);
  translate([40.0, 35.0, 40.0]) color([0.8, 0.8, 0.8, 0.85]) cube([5, 5, 5]);
  translate([35.0, 40.0, 40.0]) color([0.8, 0.8, 0.8, 0.85]) cube([5, 5, 5]);
  translate([40.0, 40.0, 40.0]) color([0.8, 0.8, 0.8, 0.85]) cube([5, 5, 5]);
}

// 零件 E
union() {
  translate([45.0, 5.0, 5.0]) color([1, 0.4, 0, 0.85]) cube([5, 5, 5]);
  translate([45.0, 10.0, 5.0]) color([1, 0.4, 0, 0.85]) cube([5, 5, 5]);
  translate([45.0, 5.0, 10.0]) color([1, 0.4, 0, 0.85]) cube([5, 5, 5]);
  translate([45.0, 10.0, 10.0]) color([1, 0.4, 0, 0.85]) cube([5, 5, 5]);
}

// 零件 A
union() {
  translate([5.0, 45.0, 5.0]) color([1, 0, 0, 0.85]) cube([5, 5, 5]);
  translate([10.0, 45.0, 5.0]) color([1, 0, 0, 0.85]) cube([5, 5, 5]);
  translate([5.0, 45.0, 10.0]) color([1, 0, 0, 0.85]) cube([5, 5, 5]);
  translate([10.0, 45.0, 10.0]) color([1, 0, 0, 0.85]) cube([5, 5, 5]);
}

// 零件 C
union() {
  translate([5.0, 5.0, 45.0]) color([0, 0.4, 1, 0.85]) cube([5, 5, 5]);
  translate([10.0, 5.0, 45.0]) color([0, 0.4, 1, 0.85]) cube([5, 5, 5]);
  translate([5.0, 10.0, 45.0]) color([0, 0.4, 1, 0.85]) cube([5, 5, 5]);
  translate([10.0, 10.0, 45.0]) color([0, 0.4, 1, 0.85]) cube([5, 5, 5]);
}

