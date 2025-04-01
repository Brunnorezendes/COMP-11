load('data.mat');
f = data.f;
t = data.t;
v = data.v;
[m, b] = identificarCruiseControl(f, t, v);
bc = b;
d = 0;
tau = 10;
Kp = (m/tau - b);
vr = 10;
hold on;
grid on;

out = sim('cruise_control_fechada.slx');
plot(out.v.time, out.v.signals.values);

bc = 0;
out = sim('cruise_control_fechada.slx');
plot(out.v.time, out.v.signals.values);

xlabel('Tempo (s)');
ylabel('Velocidade (m/s)');
title('Controle em Malha Fechada b)');
legend('bc = b', 'bc = 0');