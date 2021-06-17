default: report.pdf
.PHONY : default
report.pdf: main.tex fits_image_HD163296.png fits_image_TWHya.png TWHya_Rotate.png HD163296_Rotate.png TWHya.data.csv HD163296.data.csv references.bib
	latexmk -pdf
HD163296.data.csv: fit_map_plot.py
	python fit_map_plot.py HD163296.data
TWHya.data.csv: fit_map_plot.py
	python fit_map_plot.py TWHya.data
HD163296_Rotate.png: roatationmap_plot_data.py HD163296.data
	python roatationmap_plot_data.py HD163296.data HD163296_Rotate.png
TWHya_Rotate.png: roatationmap_plot_data.py TWHya.data
	python roatationmap_plot_data.py TWHya.data TWHya_Rotate.png
HD163296.data: roatationmap_load_data.py HD163296_CO_dv0.fits
	python roatationmap_load_data.py HD163296_CO_v0.fits HD163296_CO_dv0.fits HD163296.data
TWHya.data: roatationmap_load_data.py TWHya_CO_cube_dv0.fits
	python roatationmap_load_data.py TWHya_CO_cube_v0.fits TWHya_CO_cube_dv0.fits TWHya.data
fits_image_HD163296.png: read_fits_image.py HD163296_CO_v0.fits
	python read_fits_image.py HD163296_CO_v0.fits fits_image_HD163296.png
fits_image_TWHya.png: read_fits_image.py TWHya_CO_cube_v0.fits
	python read_fits_image.py TWHya_CO_cube_v0.fits fits_image_TWHya.png
HD163296_CO_dv0.fits: 
	wget -c https://khalidibnehasan.com/wp-content/uploads/2021/06/HD163296_CO_dv0.fits
HD163296_CO_v0.fits: 
	wget -c https://khalidibnehasan.com/wp-content/uploads/2021/06/HD163296_CO_v0.fits
TWHya_CO_cube_dv0.fits: 
	wget -c https://khalidibnehasan.com/wp-content/uploads/2021/06/TWHya_CO_cube_dv0.fits
TWHya_CO_cube_v0.fits: 
	wget -c https://khalidibnehasan.com/wp-content/uploads/2021/06/TWHya_CO_cube_v0.fits

.PHONY : clean
clean:
	rm *.csv
	rm *.png
	rm *.data
	rm *.aux
	rm *.bbl
	rm *.blg
	rm *.fdb_latexmk
	rm *.fls
	rm *.log

.PHONY : clean
deepclean:
	rm *.pdf
	rm *.fits