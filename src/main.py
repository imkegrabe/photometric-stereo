from import_modules import *

#First step: Surface Normals from Shading

#beethoven_mat = read_data_file('Beethoven.mat')
beethoven_mat = loadmat('Beethoven.mat')

#3D array I of size (m,n,k) where (m,n) is the size of each image and k is the number of views
beethoven_mat_I = beethoven_mat['I']
#2D binary array mask of size (m, n). Only pixels with values 1 should be used for Photometric stereo
beethoven_mat_mask = beethoven_mat['mask']
#an array S of light vectors, of size (k, 3), where line i represents the directional light Si that was used to obtain image I(:,:,i).
beethoven_mat_S = beethoven_mat['S']

# beethoven_mat_I.shape = (256,256,3) 
# beethoven_mat_mask.shape = (256,256)
# beethoven_mat_S.shape = (3,3)
#the amount of non-zero values in the mask  = 28898

# List of vectors with pixel values for each image, where the mask is non-zero
J = []
for i in range(0,beethoven_mat_I.shape[2]):
    J.append(beethoven_mat_I[:,:,i][np.where(beethoven_mat_mask)])
J = np.array(J)
print(J.shape)

# M = (S^−1)J to obtain the albedo modulated normal field for each image
S=np.linalg.inv(beethoven_mat_S)
M=np.dot(S,J)
#print(M.shape)

#calculting the albedo -  slide 64 ||M||
albedo = np.linalg.norm(M, axis = 0) 
#albedo.shape

#create an empty canvas for the albedo
albedo_image = np.zeros(beethoven_mat_mask.shape)
#print(albedo_image.shape)

#fill it out according to the mask
albedo_image[np.where(beethoven_mat_mask)] = albedo

#normalize M
n = (1/albedo)*M 

#split up into 3 pictures and fill out according to mask
n1 = np.zeros((beethoven_mat_mask.shape))
n1[np.where(beethoven_mat_mask)] = n[0]
n2 = np.zeros((beethoven_mat_mask.shape))
n2[np.where(beethoven_mat_mask)] = n[1]
n3 = np.zeros((beethoven_mat_mask.shape))
n3[np.where(beethoven_mat_mask)] = n[2]
n3.dtype

#Second step: Re-integration of surface from Normals with premade fumctions
#normal integration  normal + albedo simulation
z = unbiased_integrate(n1, n2, n3, beethoven_mat_mask, order = 2)

#display the 3D shape
#display_depth_mayavi(z)


#beethoven_mat = read_data_file('Beethoven.mat')
buddha = loadmat('Buddha.mat')

#3D array I of size (m,n,k) where (m,n) is the size of each image and k is the number of views
buddha_I = buddha['I']

#2D binary array mask of size (m, n). Only pixels with values 1 should be used for Photometric stereo
buddha_mask = buddha['mask']

#an array S of light vectors, of size (k, 3), where line i represents the directional light Si that was used to obtain image I(:,:,i).
buddha_S = buddha['S']

determinant_list = create_sorted_determinant_list(buddha_S)
determinant_list = sorted(determinant_list, key=lambda element: element['determinant'])
print(determinant_list)
