load('data.mat');
f = data.f;
t = data.t;
v = data.v;
[m, b] = identificarCruiseControl(f, t, v);
bc = b;
d = 0;
tau = 10;
Kp = (m/tau - b);
hold on;
grid on;

vr = 10;
out = sim('cruise_control_fechada.slx');
plot(out.v.time, out.v.signals.values);

vr = 20;
out = sim('cruise_control_fechada.slx');
plot(out.v.time, out.v.signals.values);

vr = 30;
out = sim('cruise_control_fechada.slx');
plot(out.v.time, out.v.signals.values);

xlabel('Tempo (s)');
ylabel('Velocidade (m/s)');
title('Controle em Malha Fechada a)');
legend('vr=10', 'vr=20', 'vr=30');