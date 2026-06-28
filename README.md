# 🏎️ Advanced Hydraulic Brakes & Physics Lab

Welcome to the **Advanced Hydraulic Brakes & Physics Lab**! This project is a live, interactive web application designed to simulate the mechanical engineering, fluid dynamics, and thermodynamics of a real-world automotive braking system. 

It transforms abstract physics concepts—like kinetic energy transformation and fluid power multiplication—into a visual, real-time playground.

---

## 🚀 Core Features

### 1. Live Interactive Controls
* **"Hold to Brake" Pedal:** Uses advanced event listeners to capture exact user interactions. The simulation cruises constantly until you physically click/touch and hold the red brake button, giving a tactile feel to the stopping process.
* **Real-Time Configuration Grid:** Allows users to adjust mechanical inputs on the fly before firing up the engine:
  * **Starting Speed (m/s):** Set how fast the vehicle is traveling initially.
  * **Pedal Force (N):** Adjust the physical force your foot exerts on the master cylinder.
  * **Road Friction ($\mu$):** Simulate different environments, ranging from dry asphalt ($0.9$) to slick ice ($0.1$).
  * **Cooling Rate:** Customize the rate of thermal dissipation into the surrounding air.

### 2. Dual Visualizations
* **Dynamic Test Track:** A responsive, visual track featuring an animated car element whose lateral movement speed is directly and procedurally bound to the physics engine loops.
* **Live Analytics Charting:** Powered by **Chart.js**, this dual-axis graph draws data point-by-point every half-second without layout shifting. It cleanly cross-references **Speed (m/s)** on the left axis and **Rotor Temperature (°C)** on the right axis across time.

### 3. Advanced Physics Engine Dynamics
* **Pascal's Law Integration:** Simulates real hydraulic force multiplication, scaling your input pedal force across a master-to-slave cylinder ratio.
* **Dynamic Brake Fade:** Models material limitations. If your rotor temperature surpasses **250°C**, the brake pads realistically begin to vaporize, dropping the friction coefficient and causing stopping distances to spike.
* **Tire Grip & Locked-Wheel Skidding:** Incorporates tire adhesion limits ($F = m \cdot g \cdot \mu$). Slamming the brakes too hard on low-friction surfaces causes the wheels to lock up, dropping stopping efficiency and changing the vehicle status to `SKIDDING! ⚠️`.
* **Toggleable Anti-lock Braking System (ABS):** Switch ABS on to see how an onboard computer automatically modules system pressure right at the absolute limit of tire adhesion (`ABS ENGAGED ✨`), saving the car from an uncontrolled slide.

### 4. Integrated Physics Lab Overlay
* Includes a built-in, overlay panel that pauses the active simulation loop to break down the exact mathematics governing the system under the hood. It teaches:
  * **Fluid Dynamics** (Hydraulic pressure multiplication).
  * **Thermodynamics** (Converting kinetic energy into thermal energy).
  * **Materials Science** (Thermal degradation and brake fade thresholds).
  * **Tire Dynamics** (Static vs. kinetic road friction friction limits).

---

## 🛠️ Technology Stack

* **Frontend Architecture:** Clean, semantic **HTML5** structure.
* **Styling & Layout:** **CSS3** utilizing a modern Grid/Flexbox layout, procedural transitions, and custom active state button shadows to mimic a physical pedal depression.
* **Logic Engine:** Native **JavaScript (ES6+)** running an asynchronous loop configuration via `setInterval` to handle clock cycles securely without floating-point drift.
* **Data Visualization:** **Chart.js** via an optimized Content Delivery Network (CDN) link.

---

## 📦 How to Run the Project

1. Copy the code from `index.html`.
2. Paste it into your local repository or text editor.
3. Commit and push the changes to your **GitHub Pages** repository.
4. Open your GitHub Pages URL, hit **Start Engine**, and hold down the pedal!
