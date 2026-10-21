We gathered some articles with documented shots in which the 2/1 mode was confirmed. Two main articles were used: Kuznetsov et al. (2012), Galvão et al. (2015). The shots are listed in the table below.

|Shot|Reference|Documented frequencie|Diagnostics available|
|----|-----|----|----|
|24126| Kuznetsov et al. (2012)| 13 kHz in the ohmnic phase; 14–15 kHz in the polarization phase| Mirnov, $H_\alpha$, SXR |
|24128| Kuznetsov et al. (2012), Galvão et al. (2015)| 11 kHz in the polarization phase| Mirnov, $H_\alpha$, SXR |

We then wrote a code [mdsplus_spectral_analysis.ipynb](../src/mdsplus_spectral_analysis.ipynb) that computes the Mirnov spectrogram, estimates the mode frequency as a function of time, the duration of the activity and the signal-to-noise ratio (SNR). The method is described below for shot 24126. The same parameters are applied to every coil, so that the results can be compared.

# Shot 24126

## Data and spectrograms

We accessed the data of this shot through the Yorke server. We focused on the Mirnov diagnostic and plotted the signal of the 22 Mirnov coils of TCABR as a function of time (x axis: time in ms; y axis: signal in V).

<img width="1811" height="1211" alt="final" src="https://github.com/user-attachments/assets/07387af0-fad8-4946-a3a9-c9fff98c5c37" />

From these signals we computed the STFT (Short-Time Fourier Transform) with the SciPy function of the same name, after removing the mean of each signal. We used a Hann window of 2048 samples with 75% overlap (1536 samples). The sampling frequency is about 250 kHz (Nyquist frequency of 125 kHz), which gives a window of about 8.2 ms, a frequency resolution of about 122 Hz and a step of about 2.05 ms between consecutive frames. These numbers set the limits of the whole analysis: frequencies cannot be resolved better than about 0.1 kHz, and any temporal feature (start, end or interruption of the mode) has an uncertainty of the order of the window length. A longer window would improve the frequency resolution, but it would smear the mode, since during the fastest part of the chirp the frequency changes by 1–3 kHz within a single window.

<img width="1807" height="1211" alt="especotgrama" src="https://github.com/user-attachments/assets/9f0e4fcf-db73-4794-9802-c51120ce2f28" />

In each panel the y axis is the frequency and the x axis is time. The color is the spectral power, |STFT|², in decibels: it indicates how much signal energy there is at that frequency during that time window. The dB scale is relative, since it depends on the acquisition gain and on the STFT normalization, so only differences between values (such as the SNR) are meaningful.

## Choice of the time window

The spectrograms show three distinct regimes. Before about 27 ms and after about 148 ms the noise floor is roughly 30 dB lower (about −90 to −100 dB, against about −60 dB during the plasma), and the first points of the record include samples that were added only to start the signal. At about 27 ms and between 143 and 148 ms there are broadband vertical streaks, in which all frequencies rise simultaneously, corresponding to the beginning and the end of the discharge. For these reasons the analysis is restricted to 32–140 ms, and not to the whole record. Broadband transients also occur inside the plasma (for example near 41–45, 53 and 110 ms). They are not removed by hand, but are handled by the SNR criterion described below.

## Choice of the frequency band

The mode is searched for between 10 and 20 kHz. This is where it is visible in the spectrogram of the coil used to develop the method (coil 9), and it is consistent with the documented frequencies (11–15 kHz). The band excludes the very low frequencies and the second harmonic, which is real (about 25–29 kHz between 55 and 75 ms) but is a separate structure. The same band is used for all coils, because a coherent mode must have the same frequency in all of them: a coil whose tracked frequency departs from the others indicates a tracking failure or a different structure.

## Tracking the mode

Taking the global maximum between 10 and 20 kHz at each frame fails when the mode is weak, because the maximum jumps to broadband transients or noise. Near 53 ms, for example, it jumped to about 15.5 kHz while the mode was at about 13 kHz. We therefore track the mode by continuity. The seed is the frame with the highest SNR (between about 60 and 68 ms in coil 9). From it, in each neighboring frame, forward and backward in time, the maximum is searched only within ±1 kHz of the frequency found in the previous frame. This width comes from the maximum rate of change of the mode frequency (about 0.4 kHz/ms) multiplied by the frame step (about 2 ms), which is about 0.8 kHz.

The tracker always returns a frequency, even where there is no mode (it then follows the noise maximum), so it is the SNR criterion that decides which frames are valid. As a validation, between about 55 and 75 ms the tracked frequency (12.5 to 14.8 kHz), multiplied by two, falls on the second harmonic visible at 25–29 kHz. This is an independent confirmation that the tracker follows a physical structure and not noise.

## Noise and signal-to-noise ratio

At each frame the SNR is the power of the peak minus the noise power, both in dB. The noise is the mean power (in linear scale) in a ring from 1.5 to 5 kHz on each side of the tracked frequency, which excludes the peak itself. We estimate it locally, and not in a fixed band (for example above 60 kHz), for two reasons:

- The noise is not stationary. Its power varies by about 8 dB along the analysis window.
- The noise is not white. At 65 ms the mean power above 60 kHz was −48.7 dB, against −53.7 dB between 3 and 10 kHz, and the ratio between these two bands varied by about 6 dB during the discharge. A fixed reference would bias the SNR by a different amount at each instant.

The mean is taken in linear scale and converted to dB afterwards, because the noise power in each STFT bin is exponentially distributed, and a mean taken in dB underestimates it by about 2.5 dB. A limitation is that the local noise rises near broadband transients (its maximum, about −41 dB near 41 and 55 ms, is roughly 10 dB above the typical −52 to −54 dB). There the SNR is conservative and may fall below the threshold without the mode having disappeared.

<img width="1811" height="1211" alt="f(t)" src="https://github.com/user-attachments/assets/023fcb41-5859-4462-8f77-86a1d8dfc931" />

## SNR threshold

A frame is considered to contain the mode if its SNR is above 10 dB. Since the peak is the maximum of about 17 bins (±1 kHz), noise alone does not give 0 dB. For exponentially distributed noise the expected maximum is about 5 dB above the mean, and the highest SNR we measured in the last frames (after 120 ms, where the mode is not detectable frame by frame) was 7.8 dB. The 10 dB threshold lies above both values. A lower threshold (8 dB) sits at the noise ceiling and risks false positives, while a higher one (15 dB) discards the weak decaying part of the mode.

<img width="1811" height="1211" alt="SNR_low_db" src="https://github.com/user-attachments/assets/29557a46-5ea2-4c1f-975d-4ac24cf0bd50" />

The red regions are the frames above 10 dB. An isolated frame above the threshold has no neighbor to connect to, so it appears as a single point and no red segment is visible. For this reason some parts of the curve above the dashed line are not red.

<img width="1811" height="1211" alt="tracking" src="https://github.com/user-attachments/assets/d7c64a86-02c5-4536-9485-032440238e43" />

The frequency of the mode is shown only in the valid frames, and the holes correspond to frames below the threshold. We also plotted the tracked frequency over the spectrogram:

<img width="1807" height="1211" alt="espectograma_tracado" src="https://github.com/user-attachments/assets/57cc1477-d214-4ce0-86c5-5196e4986f94" />

which confirms that the mode is followed correctly.

## Duration of the activity

The duration is defined from the frames with SNR above the threshold. Each frame covers about 8 ms, but frames are only about 2 ms apart (75% overlap). A gap of one or two frames (up to about 4 ms) is therefore shorter than the window itself and cannot be resolved as a real interruption, so gaps of up to two frames are bridged and longer gaps split the activity. The start and the end are the first and the last frame above the threshold. The uncertainty is half the difference between the interval extended by one frame on each side and the interval itself, which gives about ±2 ms (the frame step). The true temporal resolution is of the order of the window, about 8 ms.

For coil 9, with a 10 dB threshold, the activity starts at 43.0 ms and ends at 114.7 ms, a duration of 73.7 ± 2.0 ms. It consists of four continuous stretches (43.0–51.2, 55.3–73.7, 77.8–108.6 and 112.7–114.7 ms), separated by one-frame gaps near 53, 76 and 110 ms. The dependence on the threshold is shown below.

| Threshold | Start (ms) | End (ms) | Comment |
|-----------|-----------|----------|---------|
| 8 dB | 43.0 | 116.8 | one activity |
| 10 dB (reference) | 43.0 | 114.7 | one activity |
| 15 dB | 45.1 | 104.5 | splits into two activities (about 45–49 and 57–104 ms) |

The start barely depends on the threshold, because the SNR rises by about 28 dB in two frames. The end depends strongly on it, because after about 100 ms the SNR decays gradually, without a sharp edge. The end of the activity should therefore always be quoted together with the threshold. A criterion based on the largest drop of the SNR does not work here: starting from the maximum, it would stop at the first gap (near 53 ms) and again near 76 ms, leaving out the stretch at 43–51 ms and everything after about 75 ms.

## SNR and frequency results

For coil 9, the peak SNR is 34.5 dB at 59.4 ms and the mean SNR over the valid frames is 21.2 dB (a mean of the values in dB, which depends on the threshold). The median noise is −50.7 dB, with a standard deviation of 2.6 dB. The mode frequency ranges from 12.45 to 18.55 kHz, with a mean of 15.0 kHz. Within each stretch the frequency increases, and at the restarts between stretches it drops (from about 13.55 to 12.45 kHz near 53 ms, and from 14.75 to 14.05 kHz near 76 ms), which coincides with the SNR gaps. This may indicate separate events, but the gaps are shorter than the window, so we cannot confirm it. Because of the resolution of 122 Hz, plateaus such as the one at 18.55 kHz near 108–118 ms are quantization effects.

## Comparison with the literature

For this shot, Kuznetsov et al. (2012) document 13 kHz in the ohmic phase and 14–15 kHz in the polarization phase. Our tracked frequency starts at about 12.5–13.5 kHz (43–51 ms) and reaches 14–15 kHz near 73 ms, which is consistent with those values. After about 90 ms it rises to about 18.5 kHz, above the documented frequencies. Relating our time intervals to the phases of the shot (ohmic or polarization) requires the timeline of the discharge (plasma current, polarization voltage, $H_\alpha$), which is not included yet.

## Limitations

- A single coil does not give the mode numbers (m/n). The identification of the mode as 2/1 relies on the literature. With several coils, the phase differences between them would allow it to be verified.
- The method was developed on coil 9. The same parameters are applied to the others, but the detected duration depends on the sensitivity of each coil, so it is reported coil by coil.
- The time window, the frequency band and the threshold are choices. We therefore report the sensitivity to the threshold, and we note that the mode may continue beyond 20 kHz or beyond 115 ms with an SNR too low to be detected frame by frame.

| Parameter | Value |
|-----------|-------|
| Window / overlap | Hann, 2048 samples / 75% |
| Window length / frame step | ≈ 8.2 ms / ≈ 2.05 ms |
| Frequency resolution | ≈ 122 Hz |
| Time window | 32–140 ms |
| Search band | 10–20 kHz |
| Tracking half-width | 1 kHz |
| Noise ring | 1.5–5 kHz from the peak |
| SNR threshold | 10 dB |
| Gaps bridged | up to 2 frames |

# Shot 24128

Still using (link to the code) with the same parameters, we changed the shot and obtained the same graphs but for this shot now.

## Data and spectrograms

<img width="1811" height="1211" alt="final" src="https://github.com/user-attachments/assets/f4339231-30c8-42af-b193-8787f11c33fe" />

<img width="1807" height="1211" alt="especotgrama" src="https://github.com/user-attachments/assets/831a9732-e994-4318-9e0f-e9b656cd38b9" />

## Noise and signal-to-noise ratio

<img width="1811" height="1211" alt="noise" src="https://github.com/user-attachments/assets/23aae42d-713f-4c42-9c56-da5ab1204f20" />

## SNR threshold

<img width="1811" height="1211" alt="SNR_low_db" src="https://github.com/user-attachments/assets/2aff3ffc-6ef6-4d57-aa84-8a4bb5abc677" />

<img width="1811" height="1211" alt="tracking" src="https://github.com/user-attachments/assets/72f96993-f3a8-43e6-a78f-1fe9d4051a23" />

<img width="1807" height="1211" alt="espectograma_tracado" src="https://github.com/user-attachments/assets/e45b4a61-718d-4f72-a041-e26b0cbbdb17" />

All these figure and data are reproducible by using the [mdsplus_spectral_analysis.ipynb](../src/mdsplus_spectral_analysis.ipynb) and the data obtained from this analysis can be found in a table in the same code.
