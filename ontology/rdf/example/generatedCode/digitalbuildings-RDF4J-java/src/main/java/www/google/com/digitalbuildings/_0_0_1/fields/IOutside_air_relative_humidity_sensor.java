package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.IRelative;
import www.google.com.digitalbuildings._0_0_1.subfields.IHumidity;
import www.google.com.digitalbuildings._0_0_1.subfields.IAir;
import www.google.com.digitalbuildings._0_0_1.subfields.IOutside;
import www.google.com.digitalbuildings._0_0_1.subfields.ISensor;

public interface IOutside_air_relative_humidity_sensor extends IField{

	public IRI iri();

    public void addComposedOfAir (IAir parameter);

	public Set<IAir> getComposedOfAir();

    public void addComposedOfHumidity (IHumidity parameter);

	public Set<IHumidity> getComposedOfHumidity();

    public void addComposedOfOutside (IOutside parameter);

	public Set<IOutside> getComposedOfOutside();

    public void addComposedOfRelative (IRelative parameter);

	public Set<IRelative> getComposedOfRelative();

    public void addComposedOfSensor (ISensor parameter);

	public Set<ISensor> getComposedOfSensor();

}