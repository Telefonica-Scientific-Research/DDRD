# Data-Driven Deployment of Reconfigurable Intelligent Surfaces in Cellular Networks

Contact: [Sina Beyraghi](mailto:mohammadsina.beyraghi@telefonica.com)

## Description
This open-source repository includes two core methodologies: a **reflection-based algorithm** and a **scattering-based algorithm**, both designed to determine optimal RIS placement, phase configuration, and base station (BS) beam selection using site-specific simulations via Sionna RT.

### Files description

- **main.py:** Serves as the central script for configuring system and network parameters. It sequentially coordinates the simulation by invoking functions from various modular classes, enabling a structured and section-by-section execution of the complete pipeline. 
- **coverage_map.py:** Interfaces with the Sionna RT engine to compute the coverage map based on initialized ray tracing parameters. It evaluates coverage performance across the network area by processing all deployed base stations.
- **outdoor_disc.py:** Provides functionality to differentiate between indoor and outdoor users. It identifies and extracts the locations of outdoor users based on geometric and spatial analysis.
- **utils.py:** Contains utility functions for constructing and organizing base station and user data structures, facilitating efficient post-processing and analysis.
- **clustering.py:** Implements functions for applying the BIRCH clustering algorithm to group outage users based on their spatial distribution.
- **post_processing:** Provides a set of functions for organizing, filtering, and sorting simulation data across various stages of the pipeline to support analysis and visualization.
- **RayInfo:** Interfaces with Sionna RT to generate rays between specific base stations and target points. It extracts detailed ray-level information, including path types, reflection points, and interactions with surrounding buildings.
- **reflection_alg_data:** Prepares and organizes input data required for reflection-based algorithms (e.g., Strongest Ray Selection, All Ray). It outputs potential RIS deployment locations, RIS orientations, incident and desired reradiation angles, beam selection indices, and related parameters.
- **RIS_orientation:** Computes the orientation of the RIS based on the angles of the incoming and outgoing waves. It aligns the RIS surface to be practically parallel to the desired building wall, ensuring effective reflection toward the target direction.
- **strongest_ray_alg:** Implements the Strongest Ray Selection algorithm from the reflection-based approach for RIS deployment. It provides functions to jointly optimize the RIS location, base station beamforming, and RIS phase configuration for enhanced signal reflection.
- **All_ray_alg:** Implements the All Ray algorithm from the reflection-based approach for RIS deployment. It provides functions to jointly optimize the RIS location, base station beamforming, and RIS phase configuration for enhanced signal reflection.
- **RIS_Re_Assocciation:** Provides functions to re-associate remaining outage users with already deployed RIS units by establishing new line-of-sight (LoS) links, aiming to extend coverage and improve connectivity.
- **scattering_alg_data:** Prepares and organizes input data required for scattering-based algorithm. It outputs potential RIS deployment locations, RIS orientations, incident and desired reradiation angles, beam selection indices, and related parameters.
- **scattering_alg:** It provides functions to jointly optimize the RIS location, base station beamforming, and RIS phase configuration for enhanced signal reflection. It is designed to ensure a direct line-of-sight (LoS) link between the BS, RIS, and UE.
- **plotting:** Offers various plotting functions—including CDF, bar, and scatter plots—to visualize results across different simulation scenarios.


### Features
- Supports large-scale, multi-cell networks and multiple radio deployments (4G/5G/6G).
- Uses NVIDIA's **Sionna RT (v0.19.2)** for high-fidelity ray tracing.
- Joint optimization of RIS location, phase-shift configuration, and BS beamforming.
- Clustering-based user grouping for scalable RIS placement.
- Modular support for **reflection-based** and **scattering-based** RIS deployment strategies.

## How to use the code

### Cloning

Open a terminal and execute the following commands to download the github repository.

```ruby
git clone https://github.com/Telefonica-Scientific-Research/DDRD 
cd DDRD 
```

### Installation
This project requires Python 3.8+ and a complete list of dependencies is included in `requirements.txt`. 

First, create the virtual environment and activate the environment. Make sure the python version is 3.8 or higher.
```ruby
virtualenv -p python3 myenv
source myenv/bin/activate
```

Then, install the required dependencies with the following command:
```ruby
pip install -r requirements.txt
```

Finally, install torch==2.5.1 using a command similar to the one below. Depending on the CUDA version installed in your system, the command can change. Check [the official documentation](https://pytorch.org/get-started/previous-versions/) and use the command that suits the best for your system setup.
```ruby
# CUDA 12.1
pip install torch==2.5.1 torchvision==0.20.1 torchaudio==2.5.1 --index-url https://download.pytorch.org/whl/cu121
```

### Instructions to execute
The key functions of the simulation pipeline are in `main.py`. Due to the high computational complexity of the simulation, each step below must be executed sequentially rather than simultaneously. Running all components at once exceeds system memory limits. For example, the coverage map must first be simulated and its results saved (Step 2 below). Once completed, the coverage map module should be deactivated, and the outdoor_UE_disc_phase1 should be set to True and executed. After saving the results of phase 1, it should also be deactivated before running phase 2 with outdoor_UE_disc_phase2 set to True. This step-by-step workflow is essential to ensure the simulation remains executable within hardware constraints.

### Step-by-step:

1. **Deploy BS locations and area of interest**
   - You can configure deployment parameters (e.g., BS/UE location, tilt, orientation) either by reading from a .csv file or by manually specifying them in main.py. Control this behavior by setting the following line to True or False:
     https://github.com/Telefonica-Scientific-Research/DDRD/blob/76ba71a3d9d255e9b32aa621922832f94bbc0e91/main.py#L82
2. **Outdoor/Indoor User Detection**
   - Use Sionna RT to compute and save the coverage map by setting Sionna_run_maps==True and executing the main.py script. Then, set Sionna_run_maps==False and outdoor_UE_disc_phase1==True, run the main.py script again. Finally, set outdoor_UE_disc_phase1 to False and set outdoor_UE_disc_phase2==True to extract outdoor users.

      ***Important: Execute each step separately. Before running the next phase, ensure the previous one is deactivated.***

     https://github.com/Telefonica-Scientific-Research/DDRD/blob/76ba71a3d9d255e9b32aa621922832f94bbc0e91/main.py#L84-L91
3. **Clustering Outdoor Users**
   - Apply BIRCH-based clustering to group outage-prone users. Set the flag to True and run the main.py script.
     https://github.com/Telefonica-Scientific-Research/DDRD/blob/76ba71a3d9d255e9b32aa621922832f94bbc0e91/main.py#L97-L98
4. **Reflection-Based RIS Deployment**
   - Find optimal RIS placement based on ray reflection paths (Jointly optimizing BS precoder and RIS phase shift configuration). Similarly to Step 2, activate the flags accordingly and execute the main.py script again.
   
      ***Important: Execute each step separately. Before running the next phase, ensure the previous one is deactivated.***

     https://github.com/Telefonica-Scientific-Research/DDRD/blob/76ba71a3d9d255e9b32aa621922832f94bbc0e91/main.py#L100-L109
5. **Re-Clustering and Re-Deployment**
   - Re-evaluate uncovered users and repeat clustering and deployment (Jointly optimizing BS precoder and RIS phase shift configuration). 
   
      ***Important: Execute each step separately. Before running the next phase, ensure the previous one is deactivated.***

     https://github.com/Telefonica-Scientific-Research/DDRD/blob/76ba71a3d9d255e9b32aa621922832f94bbc0e91/main.py#L111-L117
6. **RIS Re-Association**
   - Re-assocciating remained outage users to nearby deployed RIS in the network (Jointly optimizing BS precoder and RIS phase shift configuration). 
   
      ***Important: Execute each step separately. Before running the next phase, ensure the previous one is deactivated.***
   
     https://github.com/Telefonica-Scientific-Research/DDRD/blob/76ba71a3d9d255e9b32aa621922832f94bbc0e91/main.py#L119-L122
7. **Optional: Scattering-Based Algorithm**
   - Repeat steps 4-6 using scattering-based logic. 

      ***Important: Execute each step separately. Before running the next phase, ensure the previous one is deactivated.***

     https://github.com/Telefonica-Scientific-Research/DDRD/blob/76ba71a3d9d255e9b32aa621922832f94bbc0e91/main.py#L128-L142

## Citation

If you find this work useful for your research, please cite our paper:

@article{beyraghi2025datadriven,
  title={Data-Driven Deployment of Reconfigurable Intelligent Surfaces in Cellular Networks},
  
  author={Beyraghi, Mohammadsina and Shabanpour, Javad and Geraci, Giovanni and Almasan, Paul and Lozano, Angel},
  
  journal={arXiv preprint arXiv:2510.10190},
  
  year={2025}
}

