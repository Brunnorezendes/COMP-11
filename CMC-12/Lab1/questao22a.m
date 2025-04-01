load('data.mat');
f = data.f;
t = data.t;
v = data.v;
[m, b] = identificarCruiseControl(f, t, v);
bc = b;
d = 0;
u = struct();
u.time = (0:0.1:100)';
u.signals.dimensions = 1;
hold on;
grid on;

vr = 10;
u.signals.values = bc*vr*ones(length(u.time), 1);
out = sim('cruise_control_aberta.slx');
plot(out.v.time, out.v.signals.values);

vr = 20;
u.signals.values = bc*vr*ones(length(u.time), 1);
out = sim('cruise_control_aberta.slx');
plot(out.v.time, out.v.signals.values);

vr = 30;
u.signals.values = bc*vr*ones(length(u.time), 1);
out = sim('cruise_control_aberta.slx');
plot(out.v.time, out.v.signals.values);

xlabel('Tempo (s)');
ylabel('Velocidade (m/s)');
title('Controle em Malha Aberta a)');
legend('vr=10', 'vr=20', 'vr=30');