load('data.mat');
f = data.f;
t = data.t;
v = data.v;
[m, b] = identificarCruiseControl(f, t, v);
bc = b;
vr = 10;
tau = 10;
Kp = (m/tau - b);
hold on;
grid on;

d = 100;
out = sim('cruise_control_fechada.slx');
plot(out.v.time, out.v.signals.values);

d = 200;
out = sim('cruise_control_fechada.slx');
plot(out.v.time, out.v.signals.values);

d = 300;
out = sim('cruise_control_fechada.slx');
plot(out.v.time, out.v.signals.values);

xlabel('Tempo (s)');
ylabel('Velocidade (m/s)');
title('Controle em Malha Fechada c)');
legend('d=100', 'd=200', 'd=300');