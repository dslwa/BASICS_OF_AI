library(magick)
library(grid)
library(gridExtra)

# Funkcja do wczytania wszystkich obrazów i masek
load_all_images_and_masks <- function(image_folder, mask_folder) {
  image_files <- list.files(image_folder, pattern = "\\.bmp$", full.names = TRUE)
  mask_files <- list.files(mask_folder, pattern = "\\.bmp$", full.names = TRUE)
  
  images <- lapply(image_files, image_read)
  masks <- lapply(mask_files, image_read)
  
  return(list(images = images, masks = masks))
}

# Funkcja do wyświetlania obrazu i maski obok siebie
show_image_and_mask <- function(image, mask) {
  # Tworzymy obiekty do wyświetlania
  obraz_grob <- rasterGrob(as.raster(image), interpolate = FALSE)
  maska_grob <- rasterGrob(as.raster(mask), interpolate = FALSE)
  
  # Wyświetlamy obie w jednym oknie obok siebie
  grid.arrange(
    grobs = list(obraz_grob, maska_grob),
    ncol = 2,
    top = "Obraz i Maska"
  )
}

# Ścieżki do folderów z obrazami i maskami
image_folder <- 'C:/Users/Don Vaporesco/Downloads/BASICS_OF_AI-main/BASICS_OF_AI-main/DatasetMerged'
mask_folder <- 'C:/Users/Don Vaporesco/Downloads/BASICS_OF_AI-main/BASICS_OF_AI-main/dataset_binarized'

# Wczytanie wszystkich obrazów i masek
all_data <- load_all_images_and_masks(image_folder, mask_folder)

# Tworzymy numerację obrazów do wyboru
image_count <- length(all_data$images)
cat("Dostępne obrazy: 1 do", image_count, "\n")

# Funkcja umożliwiająca wybór obrazu
select_and_show_image <- function() {
  # Wybór indeksu obrazu
  chosen_index <- as.integer(readline(prompt = "Wybierz numer obrazu do wyświetlenia (1 do 691): "))
  
  if (chosen_index >= 1 && chosen_index <= image_count) {
    # Wyświetlamy wybrany obraz i maskę
    show_image_and_mask(all_data$images[[chosen_index]], all_data$masks[[chosen_index]])
  } else {
    cat("Niepoprawny numer obrazu. Wybierz numer od 1 do", image_count, "\n")
  }
}

# Uruchomienie wyboru obrazu
select_and_show_image()
