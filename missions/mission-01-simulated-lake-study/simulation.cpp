#include <iostream>
#include <vector>
#include <thread>
#include <chrono>

struct DataPoint {
    int time;
    double depth;
    double temperature;
    int turbidity;
};

int main() {
    std::vector<DataPoint> missionData = {
        {0, 0.0, 22.1, 12},
        {10, 1.2, 21.9, 14},
        {20, 2.3, 21.4, 17},
        {30, 3.1, 20.8, 20},
        {40, 4.0, 20.0, 22}
    };

    std::cout << "Mission 01 – Simulated Lake Study\n";
    std::cout << "-----------------------------------\n";

    for (const auto& data : missionData) {
        std::cout << "Time: " << data.time << "s\t";
        std::cout << "Depth: " << data.depth << "m\t";
        std::cout << "Temp: " << data.temperature << "^C\t";
        std::cout << "Turbidity: " << data.turbidity << "%\n";

        std::this_thread::sleep_for(std::chrono::seconds(10));
    }

    std::cout << "\nSimulation complete.\n";
    return 0;
}
