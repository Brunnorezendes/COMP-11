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
plot(out.u.time, out.u.signals.values);

u = struct();
u.time = (0:0.1:100)';
u.signals.values = ones(length(u.time), 1);
u.signals.dimensions = 1;

for ti = 1:length(u.time)
    if ts > u.time(ti)
        u.signals.values(ti) = fmax;
    else
        u.signals.values(ti) = f;
    end
end

plot(u.time, u.signals.values);
xlabel('Tempo (s)');
ylabel('Esforço de Controle (N)');
title('Esforço de controle: Fechada x Aberta');
legend('Fechada', 'Aberta Estra. Tempo Min.');