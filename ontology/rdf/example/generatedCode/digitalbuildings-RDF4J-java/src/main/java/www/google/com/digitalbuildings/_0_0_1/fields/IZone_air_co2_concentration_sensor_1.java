package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.IZone;
import www.google.com.digitalbuildings._0_0_1.subfields.ICo2;
import www.google.com.digitalbuildings._0_0_1.subfields.IAir;
import www.google.com.digitalbuildings._0_0_1.subfields.IConcentration;
import www.google.com.digitalbuildings._0_0_1.subfields.ISensor;

public interface IZone_air_co2_concentration_sensor_1 extends IField{

	public IRI iri();

    public void addComposedOfAir (IAir parameter);

	public Set<IAir> getComposedOfAir();

    public void addComposedOfCo2 (ICo2 parameter);

	public Set<ICo2> getComposedOfCo2();

    public void addComposedOfConcentration (IConcentration parameter);

	public Set<IConcentration> getComposedOfConcentration();

    public void addComposedOfSensor (ISensor parameter);

	public Set<ISensor> getComposedOfSensor();

    public void addComposedOfZone (IZone parameter);

	public Set<IZone> getComposedOfZone();

}