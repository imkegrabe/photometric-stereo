from import_modules import*
buddha_mat = loadmat('Buddha.mat')
buddha_mat_I = buddha_mat['I']
buddha_mat_mask = buddha_mat['mask']
buddha_mat_S = buddha_mat['S']

nz = np.count_nonzero(buddha_mat_mask == 1)

determinant_list = create_sorted_determinant_list(buddha_mat_S)
determinant_list = sorted(determinant_list, key=lambda element: element['determinant'])

J = []
for i in range(3):
    J.append((buddha_mat_I[:,:,i])[np.where(buddha_mat_mask)])

J = np.array(J)

def get_light(det_list):
    light = []
    for i in det_list:
        light.append(buddha_mat_S[i])
    return np.array(light)

light = get_light(determinant_list[-1]['indices'])

S = np.linalg.pinv(light)
M = np.dot(S,J)
# M = np.linalg.pinv(light).dot(J)

albedo = np.linalg.norm(M, axis = 0) # slide 64
albedo_image = np.zeros(buddha_mat_mask.shape)
albedo_image[np.where(buddha_mat_mask)] = albedo

n = (np.linalg.norm(albedo, axis=0))*M

n1 = np.zeros((buddha_mat_mask.shape))
n1[np.where(buddha_mat_mask)] = n[0]

n2 = np.zeros((buddha_mat_mask.shape))
n2[np.where(buddha_mat_mask)] = n[1]

n3 = np.zeros((buddha_mat_mask.shape))
n3[np.where(buddha_mat_mask)] = n[2]


z = simchony_integrate(n1, n2, n3, buddha_mat_mask)
#z = np.nan_to_num(z)

#plt.imshow(z, cmap='gray')
display_depth_mayavi(z)
plt.show(block=False)
input('press <ENTER> to continue')
