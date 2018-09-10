
modes = mode(mat);
X = zeros(num_examples, num_features);

for i = 1:num_examples
    for j = 1:num_features
        if mat(i, j) ~= modes(j)
            X(i, j) = 1;
        end
    end
end

coeff = pca(X, 'NumComponents' , 3);

v0 = coeff(:, 1); 
v1 = coeff(:, 3);

x_values = zeros(num_examples , 1); 
y_values = zeros(num_examples , 1);

colors = ['y', 'm', 'c', 'r', 'g', 'b', 'k'];

for i = 1:num_examples
    x_values(i, 1) = dot(transpose(X(i, :)), v0);
    y_values(i, 1) = dot(transpose(X(i, :)), v1);
end

previousPop = population_cells{1};
previous_pop = char(previousPop); 
population_indices = zeros(); 
population_names = cell(1, 22); 
global_index = 1;

for i = 1:995
    currentPop = population_cells{i};
    current_pop = char(currentPop);
    if strcmp(previous_pop, current_pop) ~= 1
        population_names{global_index} = previous_pop ; 
        population_indices(global_index) = i ;
        global_index = global_index + 1;
    end
    previous_pop = current_pop ;
end
population_names{global_index} = previous_pop;

cell1 = cell(1, 2); cell2 = cell(1, 2); cell3 = cell(1, 2); 
cell4 = cell(1, 2); cell5 = cell(1, 2); cell6 = cell(1, 2); 
cell7 = cell(1, 2);

keysPops = {'ACB', 'GWD', 'ESN', 'MSL', 'YRI', 'LWK', 'ASW'}; 
valuesPops = {cell1 , cell2 , cell3 , cell4 , cell5 , cell6 , cell7}; 
mapObjects = containers.Map(keysPops, valuesPops);

[pop_name_m, pop_name_n] = size(population_names); % need n for size

first_index = 1;
for i = 1:pop_name_n
    currentPopName = char(population_names{i}); 
    currentCell = mapObjects(currentPopName);
    if i == pop_name_n
        last_index = num_examples;
    else
        last_index = population_indices(i) - 1; 
    end
    
    real_size = last_index - first_index + 1;
    
    if size(currentCell{1}) == 0
        currentCell{1} = x_values(first_index:last_index, 1); 
        currentCell{2} = y_values(first_index:last_index, 1);
    else
        % get size , append to end
        [currentSize_m , currentSize_n] = size(currentCell{1}); 
        tempCount = 1;
        for k = first_index:last_index
            currentCell{1}(tempCount+currentSize_m) = ...
                x_values(k,1);
            currentCell{2}(tempCount+currentSize_m) = ...
                y_values(k,1);
            tempCount = tempCount + 1;
        end
    end
    
    mapObjects(currentPopName) = currentCell; 
    if i ~= pop_name_n
        first_index = population_indices(i);
    end
end
keysPops = {'ACB', 'GWD', 'ESN', 'MSL', 'YRI', 'LWK', 'ASW'}; 
color = {'b', 'r', 'g', 'k', 'y', 'm', 'c'};
num_pops = 7;

for i = 1:num_pops
    tempCell = mapObjects(char(keysPops{i}));
    x_vals_pop = tempCell{1};
    y_vals_pop = tempCell{2};
    scatter(x_vals_pop, y_vals_pop, char(color{i}))
    hold on
end

legend('ACB', 'GWD', 'ESN', 'MSL', 'YRI', 'LWK', 'ASW')
hold off


    