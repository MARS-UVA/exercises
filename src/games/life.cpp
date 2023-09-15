//
// Created by Surya Selvam on 9/15/2023.
//

#include <iostream>
#include <vector>
#include <omp.h>
#include <unistd.h>

const int grid_size = 20;
const int num_generations = 50;

void initializeGrid(std::vector<std::vector<bool>>& grid) {
    srand(time(NULL));
    for (int i = 0; i < grid_size; i++) {
        std::vector<bool> row;
        for (int j = 0; j < grid_size; j++) {
            bool value = rand() % 2 == 1;
            row.push_back(value);
        }
        grid.push_back(row);
    }
}

void printGrid(const std::vector<std::vector<bool>>& grid) {
    for (int i = 0; i < grid_size; i++) {
        for (int j = 0; j < grid_size; j++) {
            std::cout << (grid[i][j] ? '*' : ' ') << " ";
        }
        std::cout << std::endl;
    }
}

int countLiveNeighbors(const std::vector<std::vector<bool>>& grid, int x, int y) {
    int count = 0;
    for (int i = -1; i <= 1; i++) {
        for (int j = -1; j <= 1; j++) {
            int newX = (x + i + grid_size) % grid_size;
            int newY = (y + j + grid_size) % grid_size;
            if (!(i == 0 && j == 0) && grid[newX][newY]) {
                count++;
            }
        }
    }
    return count;
}

void updateGrid(std::vector<std::vector<bool>>& grid) {
    std::vector<std::vector<bool>> newGrid(grid_size, std::vector<bool>(grid_size, false));

#pragma omp parallel for
    for (int i = 0; i < grid_size; i++) {
        for (int j = 0; j < grid_size; j++) {
            int liveNeighbors = countLiveNeighbors(grid, i, j);
            if (grid[i][j]) {
                if (liveNeighbors == 2 || liveNeighbors == 3) {
                    newGrid[i][j] = true;
                }
            } else {
                if (liveNeighbors == 3) {
                    newGrid[i][j] = true;
                }
            }
        }
    }

    grid = newGrid;
}

int main() {
    std::vector<std::vector<bool>> grid;
    initializeGrid(grid);

    for (int generation = 0; generation < num_generations; generation++) {
        system("clear");
        printGrid(grid);
        updateGrid(grid);
        usleep(100000);
    }

    return 0;
}
