package www.google.com.digitalbuildings._0_0_1.fields;

import org.eclipse.rdf4j.model.IRI;
import java.util.Set;
import www.google.com.digitalbuildings._0_0_1.subfields.IGuidevane;
import www.google.com.digitalbuildings._0_0_1.subfields.IPercentage;
import www.google.com.digitalbuildings._0_0_1.subfields.IInlet;
import www.google.com.digitalbuildings._0_0_1.subfields.ISensor;

public interface IInlet_guidevane_percentage_sensor extends IField{

	public IRI iri();

    public void addComposedOfGuidevane (IGuidevane parameter);

	public Set<IGuidevane> getComposedOfGuidevane();

    public void addComposedOfInlet (IInlet parameter);

	public Set<IInlet> getComposedOfInlet();

    public void addComposedOfPercentage (IPercentage parameter);

	public Set<IPercentage> getComposedOfPercentage();

    public void addComposedOfSensor (ISensor parameter);

	public Set<ISensor> getComposedOfSensor();

}