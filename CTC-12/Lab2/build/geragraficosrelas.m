data = load('oak_search.csv');
n = data(1:100, 2);
tseastl = data(1:100, 3);
tseaalu = data(1:100, 4);
tinsstl = data(1:100, 5);
tinsalu = data(1:100, 6);

figure;
hold on;
grid on;
p1 = polyfit(log(n), tseastl, 1);
p2 = polyfit(log(n), tseaalu, 1);
t1 = @(x) p1(2)+p1(1)*x;
t2 = @(x) p2(2)+p2(1)*x;

plot(n, tseastl);
plot(n, tseaalu);
plot(n, t1(log(n)), "b");
plot(n, t2(log(n)), "r");
title('Tempo x N para Busca');
xlabel('Tamanho N');
ylabel('Tempo (ms)');
legend('Find STL', 'Find ALU');

figure;
hold on;
grid on;
p1 = polyfit(log(n), tinsstl, 1);
p2 = polyfit(log(n), tinsalu, 1);
t1 = @(x) p1(2)+p1(1)*x;
t2 = @(x) p2(2)+p2(1)*x;
plot(n, tinsstl);
plot(n, tinsalu);
plot(n, t1(log(n)), "b");
plot(n, t2(log(n)), "r");
title('Tempo x N para Adicionar');
xlabel('Tamanho N');
ylabel('Tempo (ms)');
legend('Add STL', 'Add ALU');