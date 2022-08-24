Here is a jupyter notebook I use to automate the deconvolution or decomposition of my experimental fluorescence spectra. 

The automation takes needs to exploit a strict sample naming scheme to detect which components are in what sample. 

.. Eventually I'll add more details its a work in progress...

The procedure is essentially:

solve $Ax=b$ where $A$ is our dye component matrix $x$ are the unknown component weights and $b$ is our experimental spectra.
to solve first $A$ is factored into $Q$ and $R$, where $Q$ is orthogonal and $R$ is upper triangular.
then $Q^{T} \cdot b = y$ where $Rx = y$ can be solved by simple back substitution. 

This least squares problem can also be solved with the normal equations but I believe the QR decomposition is the most numerically stable and requires no matrix inversion. 
