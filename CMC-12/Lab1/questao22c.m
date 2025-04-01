load('data.mat');
f = data.f;
t = data.t;
v = data.v;
[m, b] = identificarCruiseControl(f, t, v);
bc = b;
vr = 10;
u = struct();
u.time = (0:0.1:100)';
u.signals.values = bc*vr*ones(length(u.time), 1);
u.signals.dimensions = 1;
hold on;
grid on;

d = 100;
out = sim('cruise_control_aberta.slx');
plot(out.v.time, out.v.signals.values);

d = 200;
out = sim('cruise_control_aberta.slx');
plot(out.v.time, out.v.signals.values);

d = 300;
out = sim('cruise_control_aberta.slx');
plot(out.v.time, out.v.signals.values);

xlabel('Tempo (s)');
ylabel('Velocidade (m/s)');
title('Controle em Malha Aberta c)');
legend('d=100', 'd=200', 'd=300');