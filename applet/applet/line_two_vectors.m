Graphics3D[{{{Thickness[0.01], Line[{{0., 0., 0.}, {5., 0., 0.}}], Text[StyleForm["x", FontSize -> 20.], {6., 0., 0.}]}, {Thickness[0.01], Line[{{0., 0., 0.}, {0., 5., 0.}}], Text[StyleForm["y", FontSize -> 20.], {0., 6., 0.}]}, {Thickness[0.01], Line[{{0., 0., 0.}, {0., 0., 5.}}], Text[StyleForm["z", FontSize -> 20.], {0., 0., 6.}]}, {Thickness[0.005], Dashing[{0.02, 0.02}], Line[{{0., 0., 0.}, {-5., 0., 0.}}]}, {Thickness[0.005], Dashing[{0.02, 0.02}], Line[{{0., 0., 0.}, {0., -5., 0.}}]}, {Thickness[0.005], Dashing[{0.02, 0.02}], Line[{{0., 0., 0.}, {0., 0., -5.}}]}}, {PointSize[0.04], RGBColor[1., 0., 0.], Point[{ax, ay, az}]}, {PointSize[0.04], RGBColor[0., 1., 0.], Point[{bx, by, bz}]}, {Thickness[0.02], RGBColor[0., 1., 0.], Line[{{ax, ay, az}, {bx, by, bz}}]}, {Thickness[0.02], RGBColor[1., 0., 0.], Line[{{0., 0., 0.}, {ax, ay, az}}]}, {Thickness[0.015], Line[{{ax - (20.*(-1.*ax + bx))/Sqrt[Abs[-1.*ax + bx]^2 + Abs[-1.*ay + by]^2 + Abs[-1.*az + bz]^2], ay - (20.*(-1.*ay + by))/Sqrt[Abs[-1.*ax + bx]^2 + Abs[-1.*ay + by]^2 + Abs[-1.*az + bz]^2], az - (20.*(-1.*az + bz))/Sqrt[Abs[-1.*ax + bx]^2 + Abs[-1.*ay + by]^2 + Abs[-1.*az + bz]^2]}, {ax + (20.*(-1.*ax + bx))/Sqrt[Abs[-1.*ax + bx]^2 + Abs[-1.*ay + by]^2 + Abs[-1.*az + bz]^2], ay + (20.*(-1.*ay + by))/Sqrt[Abs[-1.*ax + bx]^2 + Abs[-1.*ay + by]^2 + Abs[-1.*az + bz]^2], az + (20.*(-1.*az + bz))/Sqrt[Abs[-1.*ax + bx]^2 + Abs[-1.*ay + by]^2 + Abs[-1.*az + bz]^2]}}]}}, Boxed -> False, PlotRange -> {{-5., 5.}, {-5., 5.}, {-5., 5.}}, ViewPoint -> {40., 10., 20.}]