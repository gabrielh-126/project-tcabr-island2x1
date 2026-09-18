Using the [mdsplus_first_acess.ipynb](../src/mdsplus_first_acess.ipynb) function in the `src` directory, we can access the TCABR MDSplus server. For this example, we used shot 33777 and accessed the Mirnov, SXR, and $H_\alpha$ diagnostics. From these data, we identified the following available channels:

- Mirnov diagnostics: channels from 01 to 24, with nomeclature `BBMRNVN##.signal`.

- SXR diagnostics: channels from  01 to 20, with nomeclature `SOFTXR0##.signal`.

- $H_\alpha$ diagnostics: one channel, named `HALFAREF0.signal`.

For the channels investigated, each signal contains 100,000 points over a total time interval of approximately $200 ms$. The stored signals are given in voltage units ($V$). The time step is approximately $1.9989 \mu s$, corresponding to a sampling frequency of approximately $500.8 kHz$.

By taking the channels `BBMRNVN01.signal`, `SOFTXR001.signal`, and `HALFAREF0.signal`, we can plot graphs of signal x time for each one of them, whose code is located in the [mdsplus_first_acess.ipynb](../src/mdsplus_first_acess.ipynb) file. Then, we have for the Mirnov Coil N° 1:

<img width="790" height="440" alt="image" src="https://github.com/user-attachments/assets/42c9d745-1c19-4819-945e-af579f846b24" />

For the SXR signal N° 1

<img width="790" height="440" alt="image" src="https://github.com/user-attachments/assets/789dc006-bd46-43e3-a80f-9b8cc5881d5a" />

And for the reference $H_\alpha$

<img width="790" height="440" alt="image" src="https://github.com/user-attachments/assets/fe5e5e05-feef-4e3e-906c-419bf99a5d6d" />

Using the Mirnov signal, we performed a Short-Time Fourier Transform (STFT) using the `scipy.signal` library. In this method, the original time series is divided into smaller, overlapping time windows. For the present analysis, 2048 points were used in each window, with an overlap of 75% between consecutive windows. The time step between samples was calculated from the differences between consecutive time values, and the sampling frequency was then obtained from the inverse of the mean time step. For this signal, the sampling frequency is approximately 500.8 kHz. The STFT therefore allows the frequency content of the signal to be evaluated locally in time, rather than considering the entire discharge at once. 

<img width="769" height="440" alt="image" src="https://github.com/user-attachments/assets/36f22092-ba5b-4691-b0d0-9a6afdaff9c8" />

The resulting spectrogram represents the spectral power as a function of both frequency and time, $P(f,t)$. The horizontal axis represents time, the vertical axis represents frequency, and the color scale indicates the spectral power of the Mirnov signal at each frequency and instant. In the spectrogram, a horizontal structure indicates a frequency component that persists over a certain time interval, while short transient events can produce broadband structures over several frequencies. In the present shot, a prominent spectral component can be observed around 13–14 kHz during part of the discharge.

To obtain the integrated spectrum, the spectral power was integrated over a selected time interval. Mathematically, this corresponds to

$P_{int}(f) = \int_{t_1}^{t_2} P(f,t) dt$.

Thus, for each frequency, the power observed throughout the selected time interval is accumulated into a single value. The resulting graph shows which frequencies contributed most strongly to the signal during that interval. For the analyzed Mirnov signal, the integrated spectrum presents a pronounced peak around 13.7 kHz, indicating that this frequency accumulated the largest spectral contribution within the invertal of 2ms - 160ms.

<img width="790" height="440" alt="image" src="https://github.com/user-attachments/assets/cf1dac49-2005-4013-8a15-60c2c56eb102" />

