load('data.mat');
f = data.f;
t = data.t;
v = data.v;
[m, b] = identificarCruiseControl(f, t, v);
bc = b;
vr = 10;
d = 0;
f = bc*vr;
fmax = 2000;
ts = m*log(fmax/(fmax-b*vr))/b;
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
grid on;

out = sim('cruise_control_aberta.slx');
plot(out.v.time, out.v.signals.values);


xlabel('Tempo (s)');
ylabel('Velocidade (m/s)');
title('Controle em Malha Aberta b)');
legend('Estra. tempo minimo');